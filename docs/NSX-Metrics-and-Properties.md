# Collecting all metrics and properties from NSX Manager

Target: `nsxman1.liljestig.com` (192.168.150.11) · NSX **9.1.1.0** (build 25691509) · single-node manager cluster, `STABLE`
Account: `devopsro1` (role **Auditor**, read-only) · Crawl date: 2026-10-19

## 1. Answer in one paragraph

Yes. NSX has no single "dump everything" call, but every object, property and runtime metric is exposed through two REST APIs, and **the NSX Manager publishes the complete OpenAPI definition of both APIs** at `/api/v1/spec/openapi/nsx_api.json` (Manager API) and `/api/v1/spec/openapi/nsx_policy_api.json` (Policy API). Walking those specs gives a complete, version-exact list of every GET endpoint. The crawler in [`tools/nsx_crawl.py`](../tools/nsx_crawl.py) does this: it lists every collection, then substitutes the id of every object it finds into every per-object endpoint (properties, `/status`, `/state`, `/statistics`, …). Against nsxman1 it sent **13,377 read-only GET requests in 22 minutes** and covered **2,315 endpoint templates**.

## 2. Plan

| # | Step | How | Result |
|---|---|---|---|
| 1 | Store the credential safely | `Export-Clixml` (DPAPI) to `$HOME\.secrets\nsx-nsxman1.liljestig.com.xml`, the same pattern as the vCenter credential | ✅ No password in code, the repo or any command line |
| 2 | Get the authoritative endpoint list | Download both OpenAPI specs from the manager | ✅ Manager API 1,195 paths (693 GET); Policy API 2,324 paths (2,098 GET) |
| 3 | Classify endpoints | **Property** = configuration/inventory. **Metric** = last path segment is runtime data (`status`, `state`, `statistics`, `stats`, `summary`, `usage`, `capacity`, `health`, `alarms`, `realized`, `bgp`, `arp`, routing/forwarding tables, …) | ✅ 169 Manager + 509 Policy metric endpoints ([catalog](nsx-metric-endpoint-catalog.md)) |
| 4 | Filter out unsafe or useless calls | Skip deprecated endpoints, downloads (support bundles, log files, file store, CSV) and endpoints with required query parameters | ✅ 476 templates skipped, with the reason recorded |
| 5 | Resolve `{ids}` | List the parent collection (with cursor paging), take each result's `id` (fallback: `node_id`, `interface_id`, `service_name`, …), recurse | ✅ Up to 500 objects per collection |
| 6 | Collect | GET only, rate-limited to 15 req/s (NSX allows 100/s per user), retries on 429/503 | ✅ 13,377 requests, 71 MB of JSON |
| 7 | Report | [`tools/nsx_crawl_report.py`](../tools/nsx_crawl_report.py) produces outcome tables, object types and metric field names | ✅ Summarised below |

## 3. How to run it

```powershell
# one-time: store the credential (DPAPI, only this Windows user can decrypt it)
Get-Credential devopsro1 | Export-Clixml "$HOME\.secrets\nsx-nsxman1.liljestig.com.xml"

# full crawl (both APIs) -> output\<host>-<timestamp>\
./tools/Invoke-NsxCrawl.ps1 -NsxHost nsxman1.liljestig.com

# options: --api manager|policy|both  --rate 15  --max-objects 500  --include-deprecated
./tools/Invoke-NsxCrawl.ps1 -NsxHost nsxman1.liljestig.com -Out ./output/run2 --api policy --rate 25

# summary tables
python -I tools/nsx_crawl_report.py output/run2 > output/run2/report.md
```

The crawler needs only Python's standard library. The wrapper decrypts the credential and passes it to Python through the `NSX_USER` and `NSX_PASSWORD` environment variables for that one process only. Output is under `output/`, which is git-ignored because it contains lab inventory.

| Output file | Content |
|---|---|
| `spec/manager.json`, `spec/policy.json` | The exact API specs of this manager version |
| `raw/manager.jsonl`, `raw/policy.jsonl` | One JSON line per request: `template`, `url`, `status`, `ms`, `body` (the full response) |
| `endpoints.csv` | One row per GET template: `kind` (property/metric), calls, ok, errors, objects, skip reason |
| `summary.json` | Run totals |

## 4. The two APIs and where things live

| | Manager API `/api/v1` | Policy API `/policy/api/v1` |
|---|---|---|
| What it models | Fabric and platform: manager cluster and nodes, transport nodes, transport zones, compute managers, certificates, upgrade, licences, alarms, events | Desired-state networking and security: segments, Tier-0/Tier-1 gateways, groups, DFW and gateway firewall, IDS/IPS, NAT, VPN, load balancer, projects and VPCs, plus realized state |
| Best for metrics | Manager node health (CPU, memory, disk, services), transport node health (agents, tunnels, PNICs), cluster status, alarms | Per-object traffic and rule statistics (`/statistics`), realization status (`/state`, `/status`), capacity usage |
| Object id key | `id` (sometimes `node_id`) | `id`; objects are addressed by `path`, e.g. `/infra/tier-1s/t1-a` |

### 4.1 Most important metric endpoints

All of these are in the spec. ✅ means data was returned in this lab; "n/i" means the lab has **no instances** of the object yet (for example no Edges or gateways), so the endpoint could not be exercised.

| Object | Endpoint | Key fields | Lab |
|---|---|---|---|
| NSX Manager node | `GET /api/v1/node/status` | `cpu_cores`, `load_average[]`, `mem_total/used/cache`, `swap_*`, `file_systems[].total/used`, `uptime` | ✅ |
| Manager cluster | `GET /api/v1/cluster/status` | `overall_status`, `mgmt_cluster_status`, `control_cluster_status`, `detailed_cluster_status.groups[].group_status` | ✅ |
| Manager cluster nodes | `GET /api/v1/cluster/nodes/{id}/status` | `system_status.*` (CPU, memory, disk, load), `mgmt_cluster_status` | ✅ |
| Manager NICs | `GET /api/v1/cluster/nodes/{id}/network/interfaces/{if}/stats` | `rx/tx_bytes`, `rx/tx_packets`, `rx/tx_errors`, `rx/tx_dropped` | ✅ |
| Manager services | `GET /api/v1/node/services/{svc}/status` | `runtime_state`, `monitor_runtime_state`, `pids[]` | ✅ (29 services) |
| Manager top processes | `GET /api/v1/systemhealth/appliances/process/status` | `top_process_by_cpu_list[].cpu_usage`, `…_by_mem_list[].memory_usage` | ✅ |
| Alarms | `GET /api/v1/alarms` | `severity`, `status`, `feature_name`, `event_type`, `entity_id` | ✅ (4 alarms) |
| Capacity | `GET /policy/api/v1/infra/capacity/dashboard/usage` | `capacity_usage[].current_usage_count/percentage`, `max_supported_count`, `severity` | ✅ |
| Transport nodes (summary) | `GET /api/v1/transport-nodes/status` | `up_count`, `degraded_count`, `down_count`, `unknown_count` | ✅ |
| Host transport node | `GET /api/v1/transport-nodes/{id}/status` (or Policy `…/host-transport-nodes/{id}/status`) | `status`, `agent_status.*`, `control_connection_status.*`, `tunnel_status.*` incl. BFD diagnostics, `pnic_status.*`, `threat_status`, ~100 fields | ✅ (3 hosts) |
| Host transport node | `…/host-transport-nodes/{id}/state` | `state`, `node_deployment_state`, `maintenance_mode_state`, `host_switch_states[].endpoints[]` (TEP IP/MAC) | ✅ |
| Transport node NICs | `GET /api/v1/transport-nodes/{id}/network/interfaces/{if}/stats` | `rx/tx_bytes/packets/errors/dropped` | ✅ |
| Transport zones | `GET /api/v1/transport-zones/{id}/status` | `up/degraded/down/unknown_count` | ✅ (5 TZs) |
| Compute manager (vCenter) | `GET /api/v1/fabric/compute-managers/{id}/status` | `connection_status`, `registration_status`, `last_sync_time`, cert expiry | ✅ |
| DFW policy and rules | `GET /policy/api/v1/infra/domains/{d}/security-policies/{p}/statistics` | per rule: `hit_count`, `packet_count`, `byte_count`, `session_count`, `max_session_count`, `popularity_index` | ✅ |
| Transit gateway (VPC) | `GET /policy/api/v1/orgs/{o}/projects/{p}/transit-gateways/{tgw}/statistics` | `internal/external_traffic.rx/tx.total_bytes/total_packets/dropped_packets` | ✅ |
| IP blocks | `GET /policy/api/v1/infra/ip-blocks/{id}/usage` | `used_ips_count`, `available_ips_count`, `cidr_usage[]` | ✅ |
| Edge node | `…/edge-transport-nodes/{id}/status`, `/state`, `/network/interfaces/{if}/statistics` | node health, tunnels, interface counters (per spec) | n/i (no Edges) |
| Tier-0 / Tier-1 | `/infra/tier-0s/{id}/locale-services/{ls}/interfaces/{if}/statistics`, `/state`, `/routing-table`, `/forwarding-table`, `/nat/statistics` | interface rx/tx bytes, packets, drops; route tables; NAT hits | n/i (no gateways) |
| BGP | `/infra/tier-0s/{id}/locale-services/{ls}/bgp/neighbors/status` | neighbor `connection_state`, prefixes, uptime | n/i |
| Segments | `/infra/segments/{id}/statistics`, `/state`, `/ports/{port}/statistics`, `/ports/{port}/status` | rx/tx bytes, packets, drops, MAC learning, realization state | n/i (no segments) |
| Gateway firewall, IDS/IPS | `/infra/domains/{d}/gateway-policies/{p}/statistics`, `/intrusion-service-policies/{p}/statistics` | rule hits, bytes, sessions | n/i |
| VPN | `/infra/tier-0s/{id}/ipsec-vpn-services/{s}/sessions/{x}/statistics` | tunnel status, bytes, packets, SA counters | n/i |

The complete list of **678 metric endpoints**, with each one's lab outcome, is in [nsx-metric-endpoint-catalog.md](nsx-metric-endpoint-catalog.md).

### 4.2 Properties (inventory and configuration)

Properties are the list and object GETs: `GET /policy/api/v1/infra/<collection>` returns every object with all its attributes (`id`, `path`, `display_name`, `tags`, `_create_time`, `_last_modified_time`, `_revision`, plus type-specific fields). Object types found in this lab include:

| Type | Count | Type | Count |
|---|---:|---|---:|
| Host transport nodes | 3 | Security groups (`Group`) | 258 |
| Transport zones | 5 | Security policies / DFW rules | 3 / 6 |
| Compute manager (vCenter) | 1 | Services / service entries | 415 / 808 |
| VMs (Manager inventory) | 18 | Context profiles | 67 |
| VM vNICs | 18 | IDS signatures | 19,602 |
| Projects / transit gateways (VPC) | 1 / 1 | Malware-prevention signatures | 237 |
| IP blocks / IP pools | 2 / 1 | Alarms / monitoring events | 4 / 290 |
| Certificates (self-signed / signed / CA) | 5 / 3 / 1 | Role bindings / roles | 9 / 16 |

There are **no** segments, Tier-0/Tier-1 gateways, Edge nodes, load balancers or VPN services in this lab yet.

Shortcut for configuration: `GET /policy/api/v1/infra?filter=Type-<ResourceType>` (Hierarchical Policy API) returns a whole subtree in one call, for example `?filter=Type-Segment|Tier1`. That is useful for a fast config snapshot, but it does not return metrics.

## 5. Results of the crawl

| | Manager API | Policy API |
|---|---:|---:|
| GET templates in spec | 693 | 2,098 |
| Crawled | 542 | 1,773 |
| Skipped: deprecated | 94 | 123 |
| Skipped: download/blob | 48 | 107 |
| Skipped: required query parameter | 9 | 95 |
| **Returned data** | **269** (75 metric) | **434** (63 metric) |
| No instances to expand (feature unused) | 172 | 1,194 |
| HTTP errors | 104 | 147 |

### 5.1 Why some endpoints returned nothing

| Cause | Endpoints | Meaning |
|---|---:|---|
| Parent collection empty | 682 | Feature not configured (no Edges, gateways, segments, LB, VPN, NAPP, ALB, …). These endpoints will populate automatically once objects exist. |
| `global-infra` → HTTP 400 "path is invalid" | ~310 | Global Manager (NSX Federation) paths. This is a Local Manager, so they don't apply. |
| `/orgs/default/projects/default/infra/...` → HTTP 405 | ~300 | The default project is served from `/infra`, so project-scoped copies don't apply. |
| `/transport-nodes/{id}/node/...` → HTTP 500 | ~90 | Proxied "node" API calls into ESXi host transport nodes. On ESXi hosts this is not supported (it works for Edge nodes). Equivalent host data comes from `/transport-nodes/{id}/status` and `/state`. |
| `/cluster/{node-id}/node/...` not expanded | 102 | Per-cluster-node proxy of `/node/...`. The ids come from `/cluster/nodes`, which the generic resolver does not map. With a single manager node the data equals `/api/v1/node/...`, which **was** collected. |
| HTTP 403 for Auditor | 11 | `/management-plane-health`, `/infra/sites/agents/metrics`, SHA monitor and plugin details, third-party IPAM, `/node/tasks/{id}/response`. These need a higher role (for example Enterprise Admin), so ask for read access if they're needed. |
| HTTP 400 "provide `transport_node_id`" | ~20 | Endpoints that need a node filter query parameter. Add them as explicit calls if needed. |

## 6. Recommendations for an observability pipeline

1. **Don't re-crawl everything on every poll.** The full crawl took 22 minutes and is right for discovery and inventory (daily, or after changes). For metrics, poll only the ~140 metric templates that returned data (`endpoints.csv` where `kind=metric` and `ok>0`), every 1–5 minutes, plus new ones as Edges and gateways are added.
2. **Ask for realtime only when needed.** Many `/statistics` endpoints accept `?source=realtime`. The default `cached` values are refreshed by NSX about every minute, are cheaper and are fine for trending.
3. **Use the alarm and event feeds** (`/api/v1/alarms`, `/api/v1/events`) for health instead of re-deriving it from status fields.
4. **Use the Auditor role.** It covers almost everything (see 5.1 for the exceptions) and cannot change configuration.
5. **Respect API limits.** NSX defaults to 100 requests/s and 40 concurrent requests per client. The crawler uses 15/s with retry on 429/503.
6. **Re-run after building out the lab.** When Edges, Tier-0/Tier-1 gateways and segments exist, the "n/i" rows in section 4.1 will start returning data, with no code changes needed.

## 7. Files

| File | Purpose |
|---|---|
| [`tools/nsx_crawl.py`](../tools/nsx_crawl.py) | Spec-driven read-only crawler (Python stdlib only) |
| [`tools/Invoke-NsxCrawl.ps1`](../tools/Invoke-NsxCrawl.ps1) | Loads the DPAPI credential and runs the crawler |
| [`tools/nsx_crawl_report.py`](../tools/nsx_crawl_report.py) | Builds Markdown summary tables from a run |
| [`docs/nsx-metric-endpoint-catalog.md`](nsx-metric-endpoint-catalog.md) | All 678 metric endpoints with descriptions and lab outcome |
