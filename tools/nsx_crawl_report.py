"""Summarise an nsx_crawl.py output folder as Markdown tables.

Usage: python -I tools/nsx_crawl_report.py output/<run>  > report.md
"""
import collections
import csv
import json
import os
import sys


def area(template):
    parts = [p for p in template.strip("/").split("/") if p]
    if not parts:
        return "/"
    if parts[0] in ("infra", "orgs", "global-infra") and len(parts) > 1:
        # /orgs/{org}/projects/{p}/... -> orgs/projects
        return "/".join(p for p in parts[:4] if not p.startswith("{"))[:60]
    return parts[0]


def leaf_fields(obj, prefix="", out=None, depth=0):
    """Numeric/bool/str leaf paths of a JSON body (lists collapsed to [])."""
    out = set() if out is None else out
    if depth > 6:
        return out
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.startswith("_"):
                continue
            leaf_fields(v, f"{prefix}.{k}" if prefix else k, out, depth + 1)
    elif isinstance(obj, list):
        for v in obj[:3]:
            leaf_fields(v, prefix + "[]", out, depth + 1)
    else:
        out.add(prefix)
    return out


def main(run):
    rows = list(csv.DictReader(open(os.path.join(run, "endpoints.csv"), encoding="utf-8")))
    summary = json.load(open(os.path.join(run, "summary.json"), encoding="utf-8"))
    print(f"## Run summary\n\n```json\n{json.dumps(summary, indent=2)}\n```\n")

    def outcome(r):
        if r["errors"].startswith("skipped"):
            return r["errors"]
        if int(r["ok"]) > 0:
            return "returned data"
        if int(r["calls"]) == 0:
            return "no objects to expand"
        return "error " + r["errors"]

    print("## Endpoint outcomes\n")
    print("| API | Kind | Outcome | Endpoints |\n|---|---|---|---:|")
    c = collections.Counter()
    for r in rows:
        o = outcome(r)
        o = o if not o.startswith("error") else "error " + ",".join(
            sorted({e.split("x")[0] for e in r["errors"].split(";") if e}))
        c[(r["api"], r["kind"], o)] += 1
    for (a, k, o), n in sorted(c.items()):
        print(f"| {a} | {k} | {o} | {n} |")

    print("\n## Data returned per area\n")
    print("| API | Area | Property endpoints | Metric endpoints | Objects/records |\n|---|---|---:|---:|---:|")
    agg = collections.defaultdict(lambda: [0, 0, 0])
    for r in rows:
        if int(r["ok"]) == 0:
            continue
        a = agg[(r["api"], area(r["template"]))]
        a[0 if r["kind"] == "property" else 1] += 1
        a[2] += int(r["objects"])
    for (api, ar), (p, m, o) in sorted(agg.items()):
        print(f"| {api} | `{ar}` | {p} | {m} | {o} |")

    # Distinct resource types seen anywhere, with counts.
    types = collections.Counter()
    metric_fields = {}
    for api in ("manager", "policy"):
        path = os.path.join(run, "raw", f"{api}.jsonl")
        if not os.path.exists(path):
            continue
        seen_urls = set()
        for line in open(path, encoding="utf-8"):
            rec = json.loads(line)
            if rec["status"] != 200 or not isinstance(rec["body"], dict):
                continue
            body = rec["body"]
            if isinstance(body.get("results"), list) and rec["url"] not in seen_urls:
                seen_urls.add(rec["url"])
                for it in body["results"]:
                    if isinstance(it, dict) and it.get("resource_type"):
                        types[(api, it["resource_type"])] += 1
            last = rec["template"].rstrip("/").split("/")[-1]
            if last in ("statistics", "stats", "status", "state", "summary", "usage") \
                    and (api, rec["template"]) not in metric_fields:
                f = sorted(leaf_fields(body))
                if f:
                    metric_fields[(api, rec["template"])] = f

    print("\n## Object types found (resource_type in list responses)\n")
    print("| API | resource_type | Count |\n|---|---|---:|")
    for (api, t), n in sorted(types.items()):
        print(f"| {api} | {t} | {n} |")

    print("\n## Sample metric fields per metric endpoint\n")
    for (api, t), f in sorted(metric_fields.items()):
        shown = ", ".join(f"`{x}`" for x in f[:25])
        more = f" … (+{len(f) - 25})" if len(f) > 25 else ""
        print(f"- **{api}** `{t}`: {shown}{more}")


if __name__ == "__main__":
    main(sys.argv[1])
