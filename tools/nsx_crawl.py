"""Spec-driven, read-only crawler for NSX Manager.

Downloads (or reuses) the Manager API and Policy API OpenAPI specs from the
NSX Manager itself, then issues every non-deprecated GET it can resolve:

  * paths without path parameters are called directly;
  * paths with {params} are resolved by listing the parent collection and
    substituting the id of every object found (recursively), so per-object
    properties AND per-object status/state/statistics are collected.

Only GET requests are ever sent. Credentials come from the environment
(NSX_USER / NSX_PASSWORD) so they never appear on a command line or in a file.

Output (in --out):
  spec/<api>.json            the OpenAPI specs used
  raw/<api>.jsonl            one line per request: template, url, status, ms, body
  endpoints.csv              one row per GET template: kind, calls, ok, errors, objects
  summary.json               run totals
"""
import argparse
import base64
import csv
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

APIS = {
    "manager": {"spec": "/api/v1/spec/openapi/nsx_api.json", "base": "/api/v1"},
    "policy": {"spec": "/api/v1/spec/openapi/nsx_policy_api.json", "base": "/policy/api/v1"},
}

# Endpoints that are downloads, huge blobs or otherwise not inventory/metrics.
EXCLUDE = re.compile(
    r"(\?|format=csv|/csv$|file-store|support-bundle|/spec|tech-support|/logs/\{|/tasks/\{[^}]+\}/response|"
    r"/download|/export|/bundles|/upgrade-bundles|/upgrade/bundles|/certificates/[^/]+/pem)"
)

# Last path segment that marks an endpoint as runtime data (metrics/health)
# rather than configuration/properties.
METRIC_WORDS = re.compile(
    r"(status|state|statistics|stats|summary|usage|capacity|health|metrics|alarms|"
    r"realized|runtime|counters|diagnosis|heatmap|threat|bfd|bgp|routing-table|"
    r"forwarding-table|arp|mac-table|neighbors)"
)

ID_KEYS = ("id", "node_id", "interface_id", "service_name", "name", "uuid", "display_name")


def kind_of(template):
    last = template.rstrip("/").split("/")[-1]
    return "metric" if METRIC_WORDS.search(last) else "property"


class Client:
    def __init__(self, host, user, password, rate, timeout):
        self.host = host
        token = base64.b64encode(f"{user}:{password}".encode()).decode()
        self.headers = {"Authorization": f"Basic {token}", "Accept": "application/json"}
        self.ctx = ssl.create_default_context()
        # Lab managers typically use self-signed certs.
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.min_gap = 1.0 / rate
        self.timeout = timeout
        self.last = 0.0
        self.calls = 0

    def get(self, path):
        wait = self.min_gap - (time.monotonic() - self.last)
        if wait > 0:
            time.sleep(wait)
        self.last = time.monotonic()
        self.calls += 1
        req = urllib.request.Request(f"https://{self.host}{path}", headers=self.headers)
        t0 = time.monotonic()
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, context=self.ctx, timeout=self.timeout) as r:
                    data = r.read()
                    status = r.status
                break
            except urllib.error.HTTPError as e:
                status, data = e.code, e.read()
                if status in (429, 503) and attempt < 3:
                    time.sleep(2 ** attempt)
                    continue
                break
            except Exception as e:  # timeouts, resets
                status, data = 0, json.dumps({"error": str(e)}).encode()
                break
        ms = int((time.monotonic() - t0) * 1000)
        try:
            body = json.loads(data) if data else None
        except ValueError:
            body = {"_non_json": data[:2000].decode("utf-8", "replace")}
        return status, body, ms


def list_ids(body, param):
    """Extract object ids from a list response for path parameter `param`."""
    if not isinstance(body, dict) or not isinstance(body.get("results"), list):
        return []
    keys = (param.replace("-", "_"),) + ID_KEYS
    ids = []
    for item in body["results"]:
        if not isinstance(item, dict):
            continue
        for k in keys:
            if isinstance(item.get(k), (str, int)):
                ids.append(str(item[k]))
                break
    return ids


class Crawler:
    def __init__(self, client, out, max_objects, max_pages):
        self.c = client
        self.out = out
        self.max_objects = max_objects
        self.max_pages = max_pages
        self.cache = {}  # concrete path -> (status, body)
        self.stats = {}
        self.raw = {}

    def fetch(self, api, template, path):
        """GET a path (following cursors), cache it and record it."""
        if path in self.cache:
            return self.cache[path]
        status, body, ms = self.c.get(path)
        pages = 1
        while (status == 200 and isinstance(body, dict) and body.get("cursor")
               and isinstance(body.get("results"), list) and pages < self.max_pages):
            sep = "&" if "?" in path else "?"
            s2, b2, ms2 = self.c.get(f"{path}{sep}cursor={urllib.parse.quote(body['cursor'])}")
            ms += ms2
            pages += 1
            if s2 != 200 or not isinstance(b2, dict):
                break
            body["results"].extend(b2.get("results", []))
            body["cursor"] = b2.get("cursor")
        self.cache[path] = (status, body)
        st = self.stats.setdefault((api, template), {"calls": 0, "ok": 0, "errors": {}, "objects": 0})
        st["calls"] += 1
        if status == 200:
            st["ok"] += 1
            if isinstance(body, dict) and isinstance(body.get("results"), list):
                st["objects"] += len(body["results"])
            elif body is not None:
                st["objects"] += 1
        else:
            st["errors"][str(status)] = st["errors"].get(str(status), 0) + 1
        self.raw[api].write(json.dumps({"template": template, "url": path, "status": status,
                                        "ms": ms, "body": body}) + "\n")
        return status, body

    def expand(self, api, base, template):
        """Return concrete paths for a template by walking parent collections."""
        segs = template.strip("/").split("/")
        prefixes = [""]
        tprefix = ""
        for seg in segs:
            m = re.fullmatch(r"\{(.+)\}", seg)
            if not m:
                prefixes = [f"{p}/{seg}" for p in prefixes]
                tprefix += f"/{seg}"
                continue
            nxt = []
            for p in prefixes:
                _, body = self.fetch(api, tprefix, base + p)
                for i in list_ids(body, m.group(1))[: self.max_objects]:
                    nxt.append(f"{p}/{urllib.parse.quote(i, safe='')}")
            prefixes = nxt
            tprefix += f"/{seg}"
            if not prefixes:
                break
        return prefixes

    def run(self, api, spec, include_deprecated):
        base = APIS[api]["base"]
        skipped = []
        templates = []
        for path, ops in spec["paths"].items():
            g = ops.get("get")
            if not g:
                continue
            if g.get("deprecated") and not include_deprecated:
                skipped.append((path, "deprecated"))
            elif EXCLUDE.search(path):
                skipped.append((path, "excluded (download/blob)"))
            elif any(p.get("in") == "query" and p.get("required") for p in g.get("parameters", [])):
                skipped.append((path, "required query parameter"))
            else:
                templates.append(path)
        # Parents before children so collection lists are cached first.
        templates.sort(key=lambda p: (p.count("/"), p))
        for n, t in enumerate(templates, 1):
            if "{" not in t:
                self.fetch(api, t, base + t)
            else:
                paths = self.expand(api, base, t)
                if not paths:
                    self.stats.setdefault((api, t), {"calls": 0, "ok": 0, "errors": {}, "objects": 0})
                for p in paths:
                    self.fetch(api, t, base + p)
            if n % 100 == 0:
                print(f"[{api}] {n}/{len(templates)} templates, {self.c.calls} requests", flush=True)
        return templates, skipped


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--api", choices=["manager", "policy", "both"], default="both")
    ap.add_argument("--rate", type=float, default=15, help="max requests/second (NSX default limit is 100)")
    ap.add_argument("--timeout", type=float, default=60)
    ap.add_argument("--max-objects", type=int, default=500, help="max objects expanded per collection")
    ap.add_argument("--max-pages", type=int, default=50)
    ap.add_argument("--include-deprecated", action="store_true")
    a = ap.parse_args()

    user, pw = os.environ.get("NSX_USER"), os.environ.get("NSX_PASSWORD")
    if not user or not pw:
        sys.exit("Set NSX_USER and NSX_PASSWORD (use Invoke-NsxCrawl.ps1).")

    client = Client(a.host, user, pw, a.rate, a.timeout)
    crawler = Crawler(client, a.out, a.max_objects, a.max_pages)
    os.makedirs(os.path.join(a.out, "spec"), exist_ok=True)
    os.makedirs(os.path.join(a.out, "raw"), exist_ok=True)

    started = time.time()
    summary = {"host": a.host, "started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "apis": {}}
    skipped_all = []
    apis = ["manager", "policy"] if a.api == "both" else [a.api]
    for api in apis:
        status, spec, _ = client.get(APIS[api]["spec"])
        if status != 200:
            sys.exit(f"Could not download {api} spec: HTTP {status}")
        with open(os.path.join(a.out, "spec", f"{api}.json"), "w", encoding="utf-8") as f:
            json.dump(spec, f)
        summary["apis"][api] = {"version": spec.get("info", {}).get("version")}
        with open(os.path.join(a.out, "raw", f"{api}.jsonl"), "w", encoding="utf-8") as raw:
            crawler.raw[api] = raw
            templates, skipped = crawler.run(api, spec, a.include_deprecated)
        summary["apis"][api].update(templates=len(templates), skipped=len(skipped))
        skipped_all += [(api, p, why) for p, why in skipped]

    with open(os.path.join(a.out, "endpoints.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["api", "template", "kind", "calls", "ok", "errors", "objects"])
        for (api, t), st in sorted(crawler.stats.items()):
            if t == "":
                continue
            errs = ";".join(f"{k}x{v}" for k, v in sorted(st["errors"].items()))
            w.writerow([api, t, kind_of(t), st["calls"], st["ok"], errs, st["objects"]])
        for api, t, why in skipped_all:
            w.writerow([api, t, kind_of(t), 0, 0, f"skipped: {why}", 0])

    summary["requests"] = client.calls
    summary["seconds"] = int(time.time() - started)
    with open(os.path.join(a.out, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
