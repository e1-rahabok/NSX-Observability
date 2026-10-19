# NSX 9.1.1 metric endpoint catalog

Generated from the OpenAPI specs served by nsxman1 (`/api/v1/spec/openapi/*.json`).
Includes every non-deprecated GET whose last path segment names runtime data
(status, state, statistics, stats, summary, usage, capacity, health, metrics, alarms, realized, bfd, bgp, arp, routing/forwarding tables, …).

"Lab result" is the outcome of the 2026-10-19 crawl with the Auditor account `devopsro1`.

## Manager API (`/api/v1`) — 169 metric endpoints

### `alarms`

| Endpoint | Description | Lab result |
|---|---|---|
| `/alarms` | Get the list of all Alarms currently known to the system. | ✅ data (1 calls) |

### `cluster`

| Endpoint | Description | Lab result |
|---|---|---|
| `/cluster/backups/status` | Get backup status | ✅ data (1 calls) |
| `/cluster/nodes/deployments/{node-id}/status` | Returns the status of the VM creation/deletion | no instances in lab |
| `/cluster/nodes/{node-id}/network/interfaces/{interface-id}/stats` | Read the NSX Manager/Controller's Network Interface Statistics | ✅ data (2 calls) |
| `/cluster/nodes/{node-id}/repo_sync/status` | Synchronizes the repository data between nsx managers. | ✅ data (2 calls) |
| `/cluster/nodes/{node-id}/status` | Read cluster node runtime status | ✅ data (2 calls) |
| `/cluster/restore/status` | Query Restore Request Status | ✅ data (1 calls) |
| `/cluster/status` | Read Cluster Status | ✅ data (1 calls) |
| `/cluster/{cluster-node-id}/node/network/interfaces/{interface-id}/stats` | Read the Node's Network Interface Statistics | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/applianceproxy/status` | Read the Appliance Proxy service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/async_replicator/status` | Read the Async Replicator service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/auth/status` | Read auth service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/cluster_manager/status` | Read cluster boot manager service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/cm-inventory/status` | Read manager service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/controller/status` | Read controller service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/datastore/status` | Read the Corfu Server service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/datastore_nonconfig/status` | Read the Corfu Nonconfig Server service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/http/status` | Read http service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/idps-reporting/status` | Read the idps-reporting service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/install-upgrade/status` | Read NSX install-upgrade service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/liagent/status` | Read liagent service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/manager/status` | Read service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/messaging-manager/status` | Read NSX Messaging Manager service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/migration-coordinator/status` | Read migration coordinator service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/monitoring/status` | Read Monitoring service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/node-mgmt/status` | Read appliance management service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/node-stats` | Read NSX node-stats service properties | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/node-stats/status` | Read NSX node-stats service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/nsx-message-bus/status` | Read NSX Message Bus service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/nsx-platform-client/status` | Read NSX Platform Client service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/nsx-upgrade-agent/status` | Read Nsx upgrade agent service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/ntp/status` | Read NTP service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/search/status` | Read NSX Search service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/sha/status` | Read SHA service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/site_manager/status` | Read the Site Manager service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/snmp/status` | Read SNMP service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/ssh/status` | Read ssh service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/syslog/status` | Read syslog service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/services/ui-service/status` | Read ui service status | no instances in lab |
| `/cluster/{cluster-node-id}/node/status` | Read node status | no instances in lab |
| `/cluster/{cluster-node-id}/node/upgrade/progress-status` | Get upgrade progress status | no instances in lab |
| `/cluster/{cluster-node-id}/node/upgrade/status-summary` | Get upgrade status summary | no instances in lab |

### `edge-clusters`

| Endpoint | Description | Lab result |
|---|---|---|
| `/edge-clusters/{edge-cluster-id}/inter-site/status` | Get inter-site status of the edge cluster | no instances in lab |

### `fabric`

| Endpoint | Description | Lab result |
|---|---|---|
| `/fabric/compute-collections/{cc-ext-id}/member-status` | Return Host Node Status for a Compute Collection | HTTP 404x2 |
| `/fabric/compute-managers/{compute-manager-id}/state` | Get the realized state of a compute manager | ✅ data (1 calls) |
| `/fabric/compute-managers/{compute-manager-id}/status` | Return runtime status information for a compute manager | ✅ data (1 calls) |

### `licenses`

| Endpoint | Description | Lab result |
|---|---|---|
| `/licenses/action/async-query/status` | Get status of asynchronous query operation | HTTP 400x1 |
| `/licenses/licenses-usage` | Get usage report of all registered modules | ✅ data (1 calls) |
| `/licenses/licenses-usage?format=csv` | Get usage report of all registred modules in CSV format | skipped (excluded (download/blob)) |
| `/licenses/security-usage` | Get the security feature license usage report. | ✅ data (1 calls) |
| `/licenses/security-usage?format=csv` | Get the security feature license usage report in CSV format. | skipped (excluded (download/blob)) |
| `/licenses/vcf/action/async/status` | Get status of asynchronous query operation | HTTP 400x1 |

### `logical-switches`

| Endpoint | Description | Lab result |
|---|---|---|
| `/logical-switches/{logical-switch-id}/inter-site-forwarder/statistics` | Get L2 forwarder statistics | no instances in lab |

### `malware-prevention`

| Endpoint | Description | Lab result |
|---|---|---|
| `/malware-prevention/compute-collection/{compute-collection-id}/status` | Get status for MPS Compute collection. | no instances in lab |
| `/malware-prevention/teaser/status` | Registration status | ✅ data (1 calls) |
| `/malware-prevention/transport-node/{transport-node-id}/status` | Get status for MPS Transport Node. | no instances in lab |

### `management-plane-health`

| Endpoint | Description | Lab result |
|---|---|---|
| `/management-plane-health` | Get health stats for policy and the dependent services. | HTTP 403x1 |

### `node`

| Endpoint | Description | Lab result |
|---|---|---|
| `/node/network/interfaces/{interface-id}/stats` | Read the Node's Network Interface Statistics | ✅ data (2 calls) |
| `/node/services/applianceproxy/status` | Read the Appliance Proxy service status | ✅ data (1 calls) |
| `/node/services/async_replicator/status` | Read the Async Replicator service status | ✅ data (1 calls) |
| `/node/services/auth/status` | Read auth service status | ✅ data (1 calls) |
| `/node/services/cluster_manager/status` | Read cluster boot manager service status | ✅ data (1 calls) |
| `/node/services/cm-inventory/status` | Read manager service status | ✅ data (1 calls) |
| `/node/services/controller/status` | Read controller service status | ✅ data (1 calls) |
| `/node/services/datastore/status` | Read the Corfu Server service status | ✅ data (1 calls) |
| `/node/services/datastore_nonconfig/status` | Read the Corfu Nonconfig Server service status | ✅ data (1 calls) |
| `/node/services/http/status` | Read http service status | ✅ data (1 calls) |
| `/node/services/idps-reporting/status` | Read the idps-reporting service status | ✅ data (1 calls) |
| `/node/services/install-upgrade/status` | Read NSX install-upgrade service status | ✅ data (1 calls) |
| `/node/services/liagent/status` | Read liagent service status | ✅ data (1 calls) |
| `/node/services/manager/status` | Read service status | ✅ data (1 calls) |
| `/node/services/messaging-manager/status` | Read NSX Messaging Manager service status | ✅ data (1 calls) |
| `/node/services/migration-coordinator/status` | Read migration coordinator service status | ✅ data (1 calls) |
| `/node/services/monitoring/status` | Read Monitoring service status | ✅ data (1 calls) |
| `/node/services/node-mgmt/status` | Read appliance management service status | ✅ data (1 calls) |
| `/node/services/node-stats` | Read NSX node-stats service properties | ✅ data (1 calls) |
| `/node/services/node-stats/status` | Read NSX node-stats service status | ✅ data (1 calls) |
| `/node/services/nsx-message-bus/status` | Read NSX Message Bus service status | ✅ data (1 calls) |
| `/node/services/nsx-platform-client/status` | Read NSX Platform Client service status | ✅ data (1 calls) |
| `/node/services/nsx-upgrade-agent/status` | Read Nsx upgrade agent service status | ✅ data (1 calls) |
| `/node/services/ntp/status` | Read NTP service status | ✅ data (1 calls) |
| `/node/services/search/status` | Read NSX Search service status | ✅ data (1 calls) |
| `/node/services/sha/status` | Read SHA service status | ✅ data (1 calls) |
| `/node/services/site_manager/status` | Read the Site Manager service status | ✅ data (1 calls) |
| `/node/services/snmp/status` | Read SNMP service status | ✅ data (1 calls) |
| `/node/services/ssh/status` | Read ssh service status | ✅ data (1 calls) |
| `/node/services/syslog/status` | Read syslog service status | ✅ data (1 calls) |
| `/node/services/ui-service/status` | Read ui service status | ✅ data (1 calls) |
| `/node/status` | Read node status | ✅ data (1 calls) |
| `/node/upgrade/progress-status` | Get upgrade progress status | ✅ data (1 calls) |
| `/node/upgrade/status-summary` | Get upgrade status summary | ✅ data (1 calls) |

### `repository`

| Endpoint | Description | Lab result |
|---|---|---|
| `/repository/bundles/{bundle-id}/upload-status` | Get bundle upload status | skipped (excluded (download/blob)) |

### `reverse-proxy`

| Endpoint | Description | Lab result |
|---|---|---|
| `/reverse-proxy/node/health` | Gets Node health status | ✅ data (1 calls) |

### `search`

| Endpoint | Description | Lab result |
|---|---|---|
| `/search/reconcile/status` | API to get the search reconciliation status | ✅ data (1 calls) |

### `serviceinsertion`

| Endpoint | Description | Lab result |
|---|---|---|
| `/serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id}/state` | Get Service-Deployment state for Service. | no instances in lab |
| `/serviceinsertion/services/{service-id}/service-deployments/{service-deployment-id}/status` | Get a particular service deployment status. | no instances in lab |
| `/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes` | Returns list of instance runtimes of service VM being deployed | no instances in lab |
| `/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes/{instance-runtime-id}/interfaces/{interface_index}/status` | Get operational status for an interface | no instances in lab |
| `/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/state` | Get Service-Instance state for Service. | no instances in lab |
| `/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/status` | Get Service-Instance status for Service. | no instances in lab |

### `sites`

| Endpoint | Description | Lab result |
|---|---|---|
| `/sites/status` | Get overall status of the federation, including stub status | ✅ data (1 calls) |
| `/sites/switchover-status` | Get the switchover status | ✅ data (1 calls) |

### `systemhealth`

| Endpoint | Description | Lab result |
|---|---|---|
| `/systemhealth/appliances/latency/status` | Show the details of latency status for all appliances | ✅ data (1 calls) |
| `/systemhealth/appliances/process/status` | Show the details of process status in all appliances. | ✅ data (1 calls) |
| `/systemhealth/appliances/{appliance-id}/latency/status` | Show the details of process status in given appliance | no instances in lab |
| `/systemhealth/appliances/{appliance-id}/process/status` | Show the details of process status in given appliance | no instances in lab |
| `/systemhealth/container-cluster/ncp/status` | Get all the container cluster status | HTTP 201x1 |
| `/systemhealth/container-cluster/{cluster-id}/ncp/status` | Get the container cluster status by given id | no instances in lab |
| `/systemhealth/transport-nodes/{node-id}/container/agent/status` | Get the containter status on given node | no instances in lab |
| `/systemhealth/transport-nodes/{node-id}/container/hyperbus/status` | Get the containter hyperbus status on given node | no instances in lab |

### `transport-node-collections`

| Endpoint | Description | Lab result |
|---|---|---|
| `/transport-node-collections/{transport-node-collection-id}/state` | Get Transport Node collection application state | ✅ data (1 calls) |

### `transport-nodes`

| Endpoint | Description | Lab result |
|---|---|---|
| `/transport-nodes/status` | Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached. | ✅ data (1 calls) |
| `/transport-nodes/{edge-node-id}/inter-site/bgp/neighbors` | Paginated list of BGP Neighbors on edge transport node | ✅ data (3 calls) |
| `/transport-nodes/{edge-node-id}/inter-site/statistics` | Get inter-site statistics of edge node | ✅ data (3 calls) |
| `/transport-nodes/{node-id}/pnic-bond-status` | Get high-level summary of a transport node | ✅ data (3 calls) |
| `/transport-nodes/{node-id}/remote-transport-node-status` | Read status of all transport nodes with tunnel connections to transport node | ✅ data (3 calls) |
| `/transport-nodes/{node-id}/status` | Read status of a transport node | ✅ data (3 calls) |
| `/transport-nodes/{transport-node-id}/network/interfaces/{interface-id}/stats` | Read counters for transport node interfaces. | ✅ data (27 calls) |
| `/transport-nodes/{transport-node-id}/node/diagnosis` | Read edge config diagnosis | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/logical-routers/diagnosis` | Logical-routers diagnosis | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/logical-routers/{logical-router-id}/diagnosis` | Logical-router diagnosis | no instances in lab |
| `/transport-nodes/{transport-node-id}/node/network/interfaces/{interface-id}/stats` | Read the Node's Network Interface Statistics | no instances in lab |
| `/transport-nodes/{transport-node-id}/node/services/dataplane/cpu-stats` | Get NSX Edge dataplane cpu stats | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/dataplane/fw-stats` | Get NSX Edge dataplane firewall stats | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/dataplane/physical-ports/{physical-port}/stats` | Get the physical port statistics | no instances in lab |
| `/transport-nodes/{transport-node-id}/node/services/dataplane/physical-ports/{physical-port}/xstats` | Get the physical port extended statistics | no instances in lab |
| `/transport-nodes/{transport-node-id}/node/services/dataplane/qat-status` | Get NSX Edge dataplane QAT setting | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/dataplane/status` | Read NSX EdgeDatapath service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/dhcp/status` | Read NSX Edge DHCP service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/dispatcher/status` | Read NSX Edge Dispatcher service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/docker/status` | Read NSX Edge Docker service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/ipsecvpn/status` | Read NSX Edge Ipsec VPN service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/liagent/status` | Read liagent service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/local-controller/status` | Read NSX EdgeNSXA service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/metadata-proxy/status` | Read Metadata-proxy service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/nestdb/status` | Read NSX Nestdb service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/node-mgmt/status` | Read appliance management service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/nsx-control-plane-agent/status` | Read NSX Control Plane Agent service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/nsx-opsagent/status` | Read NSX OpsAgent service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/nsx-platform-client/status` | Read NSX Platform Client service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/nsx-upgrade-agent/status` | Read Nsx upgrade agent service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/ntp/status` | Read NTP service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/router-config/status` | Read NSX EdgeMSRConfig service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/router/status` | Read NSX EdgeMSR service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/security-hub/status` | Read NSX Edge security-hub service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/snmp/status` | Read SNMP service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/ssh/status` | Read ssh service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/syslog/status` | Read syslog service status | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/services/vpn/ipsec/deterministic-esp-rss/status` | Get NSX Edge IPSec Determ RSS setting | HTTP 500x3 |
| `/transport-nodes/{transport-node-id}/node/status` | Read node status | HTTP 500x3 |

### `transport-zones`

| Endpoint | Description | Lab result |
|---|---|---|
| `/transport-zones/status` | Get high-level summary of a transport zone. The service layer does not support source = realtime or cached. | ✅ data (1 calls) |
| `/transport-zones/transport-node-status` | Read status of all the transport nodes | ✅ data (1 calls) |
| `/transport-zones/transport-node-status-report` | Creates a status report of transport nodes of all the transport zones | HTTP 400x1 |
| `/transport-zones/transport-node-status-report-json` | Creates a status json report of transport nodes of all the transport zones | ✅ data (1 calls) |
| `/transport-zones/{zone-id}/status` | Get high-level summary of a transport zone | ✅ data (5 calls) |
| `/transport-zones/{zone-id}/transport-node-status` | Read status of transport nodes in a transport zone | ✅ data (5 calls) |
| `/transport-zones/{zone-id}/transport-node-status-report` | Creates a status report of transport nodes in a transport zone | HTTP 415x5 |
| `/transport-zones/{zone-id}/transport-node-status-report-json` | Creates a status json report of transport nodes in a transport zone | ✅ data (5 calls) |

### `trust-management`

| Endpoint | Description | Lab result |
|---|---|---|
| `/trust-management/oidc-uris/{id}/health` | Check the health of an OpenID Connect end-point | ✅ data (1 calls) |

### `upgrade`

| Endpoint | Description | Lab result |
|---|---|---|
| `/upgrade/bundles/{bundle-id}/status` | Get uploaded upgrade bundle status | skipped (excluded (download/blob)) |
| `/upgrade/bundles/{bundle-id}/upload-status` | Get uploaded upgrade bundle upload status | skipped (excluded (download/blob)) |
| `/upgrade/functional-state` | Get functional state of the upgrade coordinator | ✅ data (1 calls) |
| `/upgrade/nodes-summary` | Get summary of nodes | ✅ data (1 calls) |
| `/upgrade/status-summary` | Get upgrade status summary | ✅ data (1 calls) |
| `/upgrade/summary` | Get upgrade summary | ✅ data (1 calls) |
| `/upgrade/uc-upgrade-status` | Get upgrade-coordinator upgrade status | ✅ data (1 calls) |
| `/upgrade/upgrade-unit-groups-status` | Get upgrade status for upgrade unit groups | ✅ data (1 calls) |
| `/upgrade/upgrade-unit-groups/{group-id}/status` | Get upgrade status for group | ✅ data (10 calls) |
| `/upgrade/upgrade-units-stats` | Get upgrade units stats | ✅ data (1 calls) |

## Policy API (`/policy/api/v1`) — 509 metric endpoints

### `alb`

| Endpoint | Description | Lab result |
|---|---|---|
| `/alb/controller-nodes/deployments/{node-id}/status` | Returns the status of the node creation/deletion | no instances in lab |

### `cluster`

| Endpoint | Description | Lab result |
|---|---|---|
| `/cluster/backups/status` | Get backup status | ✅ data (1 calls) |

### `compliance`

| Endpoint | Description | Lab result |
|---|---|---|
| `/compliance/status` | Returns the compliance status | ✅ data (1 calls) |

### `global-infra`

| Endpoint | Description | Lab result |
|---|---|---|
| `/global-infra/bfd-profiles` | List BfdProfiles | HTTP 400x1 |
| `/global-infra/bfd-profiles/{bfd-profile-id}` | Read a BfdProfile | no instances in lab |
| `/global-infra/dhcp-server-configs/{config-id}/state` | Read DHCP server state | skipped (required query parameter) |
| `/global-infra/dhcp-server-configs/{config-id}/stats` | Read DHCP server statistics | skipped (required query parameter) |
| `/global-infra/dhcp-server-configs/{config-id}/status` | Read DHCP server status | skipped (required query parameter) |
| `/global-infra/domains/{domain-id}/gateway-policies/{gateway-policy-id}/rules/{rule-id}/statistics` | Get gateway rule statistics | no instances in lab |
| `/global-infra/domains/{domain-id}/gateway-policies/{gateway-policy-id}/statistics` | Get gateway policy statistics | no instances in lab |
| `/global-infra/domains/{domain-id}/intrusion-service-gateway-policies/{policy-id}/rules/{rule-id}/statistics` | Get IDS gateway rule statistics | no instances in lab |
| `/global-infra/domains/{domain-id}/intrusion-service-gateway-policies/{policy-id}/statistics` | Get IDS gateway policy statistics | no instances in lab |
| `/global-infra/domains/{domain-id}/intrusion-service-policies/{ids-policy-id}/rules/{rule-id}/statistics` | Get IDS-IPS rule statistics | no instances in lab |
| `/global-infra/domains/{domain-id}/intrusion-service-policies/{ids-policy-id}/statistics` | Get IDS security policy statistics | no instances in lab |
| `/global-infra/domains/{domain-id}/security-policies/{security-policy-id}/rules/{rule-id}/statistics` | Get rule statistics | no instances in lab |
| `/global-infra/domains/{domain-id}/security-policies/{security-policy-id}/statistics` | Get security policy statistics | no instances in lab |
| `/global-infra/firewall-identity-stores/{firewall-identity-store-id}/sync-stats` | Get Firewall identity store sync statistics for the given identifier | no instances in lab |
| `/global-infra/full-sync-states` | List full sync states | HTTP 400x1 |
| `/global-infra/metadata-proxies/{metadata-proxy-id}/statistics` | Get metadata proxy status | no instances in lab |
| `/global-infra/metadata-proxies/{metadata-proxy-id}/status` | Get metadata proxy status | no instances in lab |
| `/global-infra/realized-state/realized-entities` | Get list of realized objects associated with intent object | skipped (required query parameter) |
| `/global-infra/realized-state/status` | Get consolidated status of an intent object | skipped (required query parameter) |
| `/global-infra/segments/state` | Get infra segments by configuration state | HTTP 400x1 |
| `/global-infra/segments/{segment-id}/arp-proxy` | Get downlink port Address Resolution Protocol Proxies for infra segment | no instances in lab |
| `/global-infra/segments/{segment-id}/arp-proxy?format=csv` | Get downlink port Address Resolution Protocol Proxies for infra segment in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/segments/{segment-id}/arp-table` | Get ARP table from segment interface (downlink) | no instances in lab |
| `/global-infra/segments/{segment-id}/arp-table?format=csv` | Get ARP table from segment interface (downlink) in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/segments/{segment-id}/dhcp-static-bindings/{binding-id}/state` | Read DHCP static binding state | no instances in lab |
| `/global-infra/segments/{segment-id}/gateway-interface-dad-state` | Get DAD state for downlink router port on tier-0 router | no instances in lab |
| `/global-infra/segments/{segment-id}/gateway-interface-statistics` | Get statistics for downlink router port on tier-0 router | no instances in lab |
| `/global-infra/segments/{segment-id}/gateway-interface-statistics/summary` | Get statistics for downlink router port on tier-0 router | no instances in lab |
| `/global-infra/segments/{segment-id}/inter-site-forwarder/statistics` | Get infra segment cross site traffic statistics | no instances in lab |
| `/global-infra/segments/{segment-id}/mac-table` | Get infra segment MAC table | no instances in lab |
| `/global-infra/segments/{segment-id}/mac-table?format=csv` | Get infra segment MAC table in CSV | skipped (excluded (download/blob)) |
| `/global-infra/segments/{segment-id}/ports/{port-id}/mac-table` | Get MAC table for infra segment port | no instances in lab |
| `/global-infra/segments/{segment-id}/ports/{port-id}/mac-table?format=csv` | Get infra segment port MAC table in CSV | skipped (excluded (download/blob)) |
| `/global-infra/segments/{segment-id}/ports/{port-id}/state` | Get infra segment port state | no instances in lab |
| `/global-infra/segments/{segments-id}/ports/{port-id}/statistics` | Get infra segment port statistics information | no instances in lab |
| `/global-infra/segments/{segments-id}/ports/{port-id}/status` | Get infra segment port status information | no instances in lab |
| `/global-infra/segments/{segments-id}/state` | Get infra segment state information | no instances in lab |
| `/global-infra/segments/{segments-id}/statistics` | Get infra segment statistics information | no instances in lab |
| `/global-infra/settings/firewall/idfw/system-stats` | Get IDFW system statistics data | ✅ data (1 calls) |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/allocation/status` | Get a Policy Edge Cluster allocation status  under an Enforcement Point | no instances in lab |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/nat/statistics` | Get statistics for all logical router NAT rules on a policy edge transport node | no instances in lab |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/remote-tep-connectivity/bgp/neighbors` | Paginated list of BGP Neighbors on edge transport node | no instances in lab |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/remote-tep-connectivity/bgp/summary` | Get Remote TEP BGP summary of policy edge transport node. | no instances in lab |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/remote-tep-connectivity/tunnels/statistics` | Get cross-site tunnel statistics of policy edge transport node. | no instances in lab |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/remote-tep-connectivity/bgp/summary` | Get RTEP span and mac address-table | no instances in lab |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/remote-tep-connectivity/status` | Get a Policy Edge Cluster Remote TEP Connectivity status under an Enforcement Point | no instances in lab |
| `/global-infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/status` | Get a Policy Edge Cluster real time status  under an Enforcement Point | skipped (required query parameter) |
| `/global-infra/tier-0s/{tier-0-id}/arp-proxies` | Get Tier-0 Address Resolution Protocol Proxies | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/arp-proxies?format=csv` | Get Tier-0 Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-0s/{tier-0-id}/dns-forwarder/statistics` | Get tier-0 DNS forwarder statistics | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/dns-forwarder/status` | Get current status of tier-0 DNS forwarder | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/forwarding-table` | Get forwarding table from tier-0 | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/forwarding-table?format=csv` | Get forwarding table from tier-0 in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp` | Read BGP routing config | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp/neighbors` | List BGP neighbor configurations | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp/neighbors/status` | Get BGP neighbor status for the Tier0 | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interface-groups/{interface-group-id}/statistics` | Get tier-0 interface group statistics information | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy` | Get Tier-0 Interface Address Resolution Protocol Proxies | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy?format=csv` | Get Tier-0 Interface Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table` | Get ARP table from tier-0 interface | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table?format=csv` | Get ARP table from tier-0 interface in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/dad-state` | Get DAD status by interface | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics` | Get tier-0 interface statistics information | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics/summary` | Get tier-0 interface statistics summary information | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/nat/statistics` | List NAT Rules Statistics | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/nat/{nat-id}/nat-rules/{nat-rule-id}/statistics` | Get NAT Rule Statistics | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/routing-table` | Get routing table from tier-0 | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/routing-table?format=csv` | Get routing table from tier-0 in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-0s/{tier-0-id}/state` | Get Tier0 state | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/static-routes/bfd-peers` | List StaticRouteBfdPeers | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/static-routes/bfd-peers/{bfd-peer-id}` | Read a StaticRouteBfdPeer | no instances in lab |
| `/global-infra/tier-0s/{tier-0-id}/tier-1-interface/arp-table` | Get tier-0 router link arp information | skipped (required query parameter) |
| `/global-infra/tier-0s/{tier-0-id}/tier-1-interface/arp-table?format=csv` | Get ARP table from tier-0 router link interface in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-0s/{tier-0-id}/tier-1-interface/statistics` | Get tier-0 router link statistics information | skipped (required query parameter) |
| `/global-infra/tier-0s/{tier-0-id}/tier-1-interface/statistics/summary` | Get tier-0 router link statistics summary information | skipped (required query parameter) |
| `/global-infra/tier-1s/{tier-1-id}/arp-proxies` | Get Tier-1 Address Resolution Protocol Proxies | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/arp-proxies?format=csv` | Get Tier-1 Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/dns-forwarder/statistics` | Get tier-1 DNS forwarder statistics | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/dns-forwarder/status` | Get current status of tier-1 DNS forwarder | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/forwarding-table` | Get forwarding table from tier-1 | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/forwarding-table?format=csv` | Get forwarding table from tier-1 in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interface-groups/{interface-group-id}/statistics` | Get tier-1 interface group statistics information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy` | Get Tier-1 Interface Address Resolution Protocol Proxies | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy?format=csv` | Get Tier-1 Interface Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table` | Get ARP table from tier-1 interface | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table?format=csv` | Get ARP table from tier-1 interface in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/dad-state` | Get DAD status by interface | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics` | Get tier-1 interface statistics information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics/summary` | Get tier-1 interface statistics summary information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/locale-services/{locale-services-id}/inter-site-forwarder/status` | Get inter-site L2 forwarder status for Tier1 gateway | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/nat/statistics` | List NAT Rules Statistics | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules/{nat-rule-id}/statistics` | Get NAT Rule Statistics | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/state` | Get tier-1 segments by configuration state | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-proxy` | Get downlink port Address Resolution Protocol Proxies for tier-1 segment | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-proxy?format=csv` | Get downlink port Address Resolution Protocol Proxies for tier-1 segment in CSV | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-table` | Get ARP table from segment interface (downlink) | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-table?format=csv` | Get ARP table from segment interface (downlink) in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/bep-statistics` | Get Tier-1 segment bridge end point statistics using segment ID and profile path. | skipped (required query parameter) |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/bep-status` | Get Tier-1 segment bridge end point status using segment ID and profile path. | skipped (required query parameter) |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/dhcp-static-bindings/{binding-id}/state` | Read DHCP static binding state | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-dad-state` | Get DAD state for downlink router port on tier-1 router | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-statistics` | Get statistics for downlink router port on tier-1 router | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-statistics/summary` | Get statistics for downlink router port on tier-1 router | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/inter-site-forwarder/statistics` | Get segment cross site traffic statistics | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/mac-table` | Get Tier-1 segment MAC table | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/mac-table?format=csv` | Get Tier-1 segment MAC table in CSV | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/mac-table` | Get MAC table for tier-1 segment port | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/mac-table?format=csv` | Get tier-1 segment port MAC table in CSV | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/state` | Get tier-1  segment port state | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segment-id}/static-arp` | Read static ARP config | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segments-id}/ports/{port-id}/statistics` | Get tier-1 segment port statistics information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segments-id}/ports/{port-id}/status` | Get segment port status information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segments-id}/state` | Get segment state information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/segments/{segments-id}/statistics` | Get segment statistics information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/state` | Get Tier1 state | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/tier-0-interface/arp-table` | Get tier-1 router link arp information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/tier-0-interface/arp-table?format=csv` | Get ARP table from tier-1 router link interface in CSV format | skipped (excluded (download/blob)) |
| `/global-infra/tier-1s/{tier-1-id}/tier-0-interface/statistics` | Get tier-1 router link statistics information | no instances in lab |
| `/global-infra/tier-1s/{tier-1-id}/tier-0-interface/statistics/summary` | Get tier-1 router link statistics summary information | no instances in lab |

### `infra`

| Endpoint | Description | Lab result |
|---|---|---|
| `/infra/antrea/traceflows/{traceflow-id}/status` | Read Antrea traceflow status | no instances in lab |
| `/infra/auto-health-check-toggle` | Get automatic health check toggle | ✅ data (1 calls) |
| `/infra/auto-health-checks` | Get automatic health checks | ✅ data (1 calls) |
| `/infra/bfd-profiles` | List BfdProfiles | ✅ data (1 calls) |
| `/infra/bfd-profiles/{bfd-profile-id}` | Read a BfdProfile | ✅ data (2 calls) |
| `/infra/capacity/dashboard/usage` | Returns capacity usage data for NSX objects | ✅ data (1 calls) |
| `/infra/dhcp-server-configs/{config-id}/state` | Read DHCP server state | skipped (required query parameter) |
| `/infra/dhcp-server-configs/{config-id}/stats` | Read DHCP server statistics | skipped (required query parameter) |
| `/infra/dhcp-server-configs/{config-id}/status` | Read DHCP server status | skipped (required query parameter) |
| `/infra/domains/{domain-id}/bridge-policies/{bridge-firewall-policy-id}/rules/{rule-id}/statistics` | Get bridge firewall rule statistics | no instances in lab |
| `/infra/domains/{domain-id}/bridge-policies/{bridge-firewall-policy-id}/statistics` | Get bridge firewall policy statistics | no instances in lab |
| `/infra/domains/{domain-id}/gateway-policies/{gateway-policy-id}/rules/{rule-id}/statistics` | Get gateway rule statistics | no instances in lab |
| `/infra/domains/{domain-id}/gateway-policies/{gateway-policy-id}/statistics` | Get gateway policy statistics | no instances in lab |
| `/infra/domains/{domain-id}/groups/{group-id}/group-monitoring-profile-binding-maps/{group-monitoring-profile-binding-map-id}/mirror-stack-status` | Get mirror stack status for Group Monitoring Profile Binding Map. | no instances in lab |
| `/infra/domains/{domain-id}/intrusion-service-gateway-policies/{policy-id}/rules/{rule-id}/statistics` | Get IDS gateway rule statistics | no instances in lab |
| `/infra/domains/{domain-id}/intrusion-service-gateway-policies/{policy-id}/statistics` | Get IDS gateway policy statistics | no instances in lab |
| `/infra/domains/{domain-id}/intrusion-service-policies/{ids-policy-id}/rules/{rule-id}/statistics` | Get IDS-IPS rule statistics | no instances in lab |
| `/infra/domains/{domain-id}/intrusion-service-policies/{ids-policy-id}/statistics` | Get IDS security policy statistics | no instances in lab |
| `/infra/domains/{domain-id}/security-policies/{security-policy-id}/rules/{rule-id}/statistics` | Get rule statistics | HTTP 400x1;404x5 |
| `/infra/domains/{domain-id}/security-policies/{security-policy-id}/statistics` | Get security policy statistics | ✅ data (2 calls) |
| `/infra/firewall-identity-stores/{firewall-identity-store-id}/sync-stats` | Get Firewall identity store sync statistics for the given identifier | no instances in lab |
| `/infra/full-sync-states` | List full sync states | ✅ data (1 calls) |
| `/infra/ip-blocks/allocation-state` | IpAddressBlocks allocation states | ✅ data (1 calls) |
| `/infra/ip-blocks/state` | Get state of the given IpAddressBlock | skipped (required query parameter) |
| `/infra/ip-blocks/usage` | Usage Details for all IpAddressBlocks | ✅ data (1 calls) |
| `/infra/ip-blocks/{ip-block-id}/allocation-state` | IpAddressBlock allocation state | ✅ data (2 calls) |
| `/infra/ip-blocks/{ip-block-id}/usage` | Get an IpAddressBlock usage | ✅ data (2 calls) |
| `/infra/lb-node-usage` | Read load balancer usage for the given node | skipped (required query parameter) |
| `/infra/lb-node-usage-summary` | Read load balancer node usage summary | ✅ data (1 calls) |
| `/infra/lb-service-usage-summary` | Read load balancer service usage summary | ✅ data (1 calls) |
| `/infra/lb-services/{lb-service-id}/detailed-status` | Get LBService status information | no instances in lab |
| `/infra/lb-services/{lb-service-id}/lb-pools/{lb-pool-id}/detailed-status` | Get LBPool status information | no instances in lab |
| `/infra/lb-services/{lb-service-id}/lb-pools/{lb-pool-id}/statistics` | Get LBPool statistics information | no instances in lab |
| `/infra/lb-services/{lb-service-id}/lb-virtual-servers/{lb-virtual-server-id}/detailed-status` | Get LBVirtualServer status information | no instances in lab |
| `/infra/lb-services/{lb-service-id}/lb-virtual-servers/{lb-virtual-server-id}/statistics` | Get LBVirtualServer statistics information | no instances in lab |
| `/infra/lb-services/{lb-service-id}/service-usage` | Get LBService usage information | no instances in lab |
| `/infra/lb-services/{lb-service-id}/statistics` | Get LBService statistics information | no instances in lab |
| `/infra/limits/state` | Get consumption details and other operational state for limits | ✅ data (1 calls) |
| `/infra/limits/{limit-id}/state` | Get consumption details and other operational state for a limit | no instances in lab |
| `/infra/livetraces/statuses` | List livetrace status entities | ✅ data (1 calls) |
| `/infra/livetraces/{livetrace-id}/status` | Read livetrace status | no instances in lab |
| `/infra/manual-health-checks` | List all the manual health check config entities | ✅ data (1 calls) |
| `/infra/manual-health-checks/{manual-health-check-id}` | Get a manual health check config | no instances in lab |
| `/infra/metadata-proxies/{metadata-proxy-id}/statistics` | Get metadata proxy status | no instances in lab |
| `/infra/metadata-proxies/{metadata-proxy-id}/status` | Get metadata proxy status | no instances in lab |
| `/infra/realized-state/alarms` | List All alarms in the system | ✅ data (1 calls) |
| `/infra/realized-state/realized-entities` | Get list of realized objects associated with intent object | skipped (required query parameter) |
| `/infra/realized-state/realized-entity` | Get realized entity uniquely identified by realized path | skipped (required query parameter) |
| `/infra/realized-state/status` | Get consolidated status of an intent object | skipped (required query parameter) |
| `/infra/route-controllers/{route-controller-id}/bgp/neighbors/status` | Get BGP neighbor status for the route controller | no instances in lab |
| `/infra/route-controllers/{route-controller-id}/forwarding-table` | Get forwarding table from route controller | no instances in lab |
| `/infra/route-controllers/{route-controller-id}/interfaces/{interface-id}/statistics` | Get policy route controller interface statistics for given interface-id | no instances in lab |
| `/infra/route-controllers/{route-controller-id}/interfaces/{interface-id}/statistics/summary` | Get policy route controller interface statistics summary for given interface-id | no instances in lab |
| `/infra/route-controllers/{route-controller-id}/routing-table` | Get routing table from route controller | no instances in lab |
| `/infra/route-controllers/{route-controller-id}/state` | Get the route controller state | no instances in lab |
| `/infra/route-controllers/{router-controller-id}/bgp` | Read a BGP routing config | no instances in lab |
| `/infra/route-controllers/{router-controller-id}/bgp/neighbors` | List BGP neighbor configs | no instances in lab |
| `/infra/segments/state` | Get infra segments by configuration state | HTTP 400x1 |
| `/infra/segments/{infra-segment-id}/ports/{infra-port-id}/port-monitoring-profile-binding-maps/{port-monitoring-profile-binding-map-id}/mirror-stack-status` | Get mirror stack status for Infra Port Monitoring Profile Binding Map | no instances in lab |
| `/infra/segments/{infra-segment-id}/segment-monitoring-profile-binding-maps/{segment-monitoring-profile-binding-map-id}/mirror-stack-status` | Get Infra Segment Monitoring Profile Binding Map | no instances in lab |
| `/infra/segments/{segment-id}/arp-proxy` | Get downlink port Address Resolution Protocol Proxies for infra segment | no instances in lab |
| `/infra/segments/{segment-id}/arp-proxy?format=csv` | Get downlink port Address Resolution Protocol Proxies for infra segment in CSV format | skipped (excluded (download/blob)) |
| `/infra/segments/{segment-id}/arp-table` | Get ARP table from segment interface (downlink) | no instances in lab |
| `/infra/segments/{segment-id}/arp-table?format=csv` | Get ARP table from segment interface (downlink) in CSV format | skipped (excluded (download/blob)) |
| `/infra/segments/{segment-id}/bep-statistics` | Get infra segment bridge end point statistics using segment ID and profile path. | skipped (required query parameter) |
| `/infra/segments/{segment-id}/bep-status` | Get Tier-1 segment bridge end point status using segment ID and profile path. | skipped (required query parameter) |
| `/infra/segments/{segment-id}/dhcp-static-bindings/{binding-id}/state` | Read DHCP static binding state | no instances in lab |
| `/infra/segments/{segment-id}/gateway-interface-dad-state` | Get DAD state for downlink router port on tier-0 router | no instances in lab |
| `/infra/segments/{segment-id}/gateway-interface-statistics` | Get statistics for downlink router port on tier-0 router | no instances in lab |
| `/infra/segments/{segment-id}/gateway-interface-statistics/summary` | Get statistics for downlink router port on tier-0 router | no instances in lab |
| `/infra/segments/{segment-id}/mac-table` | Get infra segment MAC table | no instances in lab |
| `/infra/segments/{segment-id}/mac-table?format=csv` | Get infra segment MAC table in CSV | skipped (excluded (download/blob)) |
| `/infra/segments/{segment-id}/ports/{port-id}/mac-table` | Get MAC table for infra segment port | no instances in lab |
| `/infra/segments/{segment-id}/ports/{port-id}/mac-table?format=csv` | Get infra segment port MAC table in CSV | skipped (excluded (download/blob)) |
| `/infra/segments/{segment-id}/ports/{port-id}/state` | Get infra segment port state | no instances in lab |
| `/infra/segments/{segments-id}/ports/{port-id}/statistics` | Get infra segment port statistics information | no instances in lab |
| `/infra/segments/{segments-id}/ports/{port-id}/status` | Get infra segment port status information | no instances in lab |
| `/infra/segments/{segments-id}/state` | Get infra segment state information | no instances in lab |
| `/infra/segments/{segments-id}/statistics` | Get infra segment statistics information | no instances in lab |
| `/infra/settings/firewall/idfw/compute-collections/status` | Get IDFW status for all Compute Collections | ✅ data (1 calls) |
| `/infra/settings/firewall/idfw/compute-collections/{compute-collection-id}/status` | Get IDFW status for a Compute Collection | no instances in lab |
| `/infra/settings/firewall/idfw/compute-collections/{compute-collection-id}/transport-nodes/status` | List IDFW status for Transport Nodes in a Compute Collection | no instances in lab |
| `/infra/settings/firewall/idfw/system-stats` | Get IDFW system statistics data | ✅ data (1 calls) |
| `/infra/settings/firewall/idfw/transport-nodes/{transport-node-id}/vms/status` | List IDFW status of VMs by transport node id | no instances in lab |
| `/infra/settings/firewall/security/intrusion-services/signatures/status` | Get IDS signature status | ✅ data (1 calls) |
| `/infra/settings/firewall/security/intrusion-services/signatures/vtis-bundle-status` | Checks if there is a new bundle available on vtis | HTTP 400x1 |
| `/infra/settings/scrx/cluster-configs/{cluster-id}/status` | Get SCRX resize status for a cluster. | no instances in lab |
| `/infra/settings/service-insertion/security/status` | Get service insertion configuration status | ✅ data (1 calls) |
| `/infra/sha/appliances/latency/status` | Get the details of latency status for all appliances | ✅ data (1 calls) |
| `/infra/sha/appliances/process/status` | Get the list of process status for all appliances. | ✅ data (1 calls) |
| `/infra/sha/appliances/{appliance-id}/latency/status` | Get the details of latency status in given appliance. | no instances in lab |
| `/infra/sha/appliances/{appliance-id}/process/status` | Get the details of process status in given appliance. | no instances in lab |
| `/infra/sha/dynamic-runbook-instances/{instance-id}/state` | Read a Dynamic Runbook Instance state | no instances in lab |
| `/infra/sha/monitors-status` | List the status of SHA monitors | HTTP 400x1 |
| `/infra/sha/monitors/{monitor-id}/status` | Read the SHA monitor status | HTTP 400x19 |
| `/infra/site/offboarding-status` | Get site offboarding status. | HTTP 404x1 |
| `/infra/sites/agents/metrics` | Fetch current Metric agent config | HTTP 403x1 |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/container-cluster-ncpstatus` | Get all the container cluster status | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/container-cluster/{cluster-id}/ncpstatus` | Get the container cluster status by given id | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/host-transport-nodes-aggstatus` | Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached. | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/host-transport-nodes-status` | Read status of all the transport nodes | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/host-transport-nodes/{node-id}/hyperbus-status` | Get the container hyperbus status on given node | ✅ data (3 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/host-transport-nodes/{node-id}/node-agent-status` | Get the container status on given node | ✅ data (3 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/host-transport-nodes/{node-id}/pnic-bond-status` | Get high-level summary of a transport node | ✅ data (3 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/host-transport-nodes/{node-id}/remote-transport-node-status` | Read status of all transport nodes with tunnel connections to transport node | ✅ data (3 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/host-transport-nodes/{node-id}/status` | Read status of a transport node | ✅ data (3 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/transport-node-status-report` | Creates a status report of transport nodes of all the transport zones | HTTP 415x1 |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/transport-node-status-report-json` | Creates a status json report of transport nodes of all the transport zones | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/transport-zones-aggstatus` | Get high-level summary of all transport zone status. The service layer does not support source = realtime or cached. | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/transport-zones/{zone-id}/status` | Get high-level summary of a transport zone | ✅ data (5 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/transport-zones/{zone-id}/transport-node-status` | Read status of transport nodes in a transport zone | ✅ data (5 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/transport-zones/{zone-id}/transport-node-status-report` | Creates a status report of transport nodes in a transport zone | HTTP 415x5 |
| `/infra/sites/{site-id}/enforcement-points/{enforcement-point-id}/transport-zones/{zone-id}/transport-node-status-report-json` | Creates a status json report of transport nodes in a transport zone | ✅ data (5 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/bm-ccpn-status` | Read BMC cluster status list | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/bm-ccpn/{cluster-control-plane-id}/status` | Read BMC cluster status | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/cluster-control-planes-status` | Read Antrea cluster status list | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/cluster-control-planes/{cluster-control-plane-id}/status` | Read Antrea cluster status | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/allocation/status` | Get a Policy Edge Cluster allocation status  under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/nat/statistics` | Get statistics for all logical router NAT rules on a policy edge transport node | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/remote-tep-connectivity/bgp/neighbors` | Paginated list of BGP Neighbors on edge transport node | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/remote-tep-connectivity/bgp/summary` | Get Remote TEP BGP summary of policy edge transport node. | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/edge-nodes/{policy-edge-node-id}/remote-tep-connectivity/tunnels/statistics` | Get cross-site tunnel statistics of policy edge transport node. | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/remote-tep-connectivity/bgp/summary` | Get RTEP span and mac address-table | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/remote-tep-connectivity/status` | Get a Policy Edge Cluster Remote TEP Connectivity status under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/state` | Get a Policy Edge Cluster State info under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-clusters/{edge-cluster-id}/status` | Get a Policy Edge Cluster real time status  under an Enforcement Point | skipped (required query parameter) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-transport-nodes/state` | Get a Policy EdgeTransport Node's State info under an Enforcement Point | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-transport-nodes/status` | Get high-level summary of all edge transport nodes. The service layer does not support source = realtime or cached. | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-transport-nodes/{edge-transport-node-id}/network/interfaces/{interface-id}/statistics` | Read counters for edge transport node interfaces. | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-transport-nodes/{edge-transport-node-id}/state` | Get a Policy EdgeTransport Node's State info under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-transport-nodes/{edge-transport-node-id}/status` | Get a Policy EdgeTransport Node's status info under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/edge-transport-nodes/{node-id}/nat/statistics` | Get statistics for all logical router NAT rules on a edge transport node | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/host-transport-nodes/state` | List transport nodes by realized state | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/host-transport-nodes/{host-transport-node-id}/state` | Get a Host Transport Node's State | ✅ data (3 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/host-transport-nodes/{host-transport-node-id}/vteps/actions/status` | List all TransportNode VTEP actions' status | ✅ data (3 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/transport-node-collections/{transport-node-collection-id}/state` | Get Transport Node collection application state | ✅ data (1 calls) |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/virtual-network-appliance-clusters/{virtual-network-appliance-cluster-id}/allocation/status` | Get a virtual network appliance cluster allocation status under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/virtual-network-appliance-clusters/{virtual-network-appliance-cluster-id}/state` | Get a Policy VirtualNetworkAppliance Cluster State info under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/virtual-network-appliance-clusters/{virtual-network-appliance-cluster-id}/status` | Get a virtual network appliance Cluster real time status under an Enforcement Point | no instances in lab |
| `/infra/sites/{site-id}/enforcement-points/{enforcementpoint-id}/virtual-network-appliance-clusters/{virtual-network-appliance-cluster-id}/virtual-network-appliances/{virtual-network-appliance-id}/state` | Get a Virtual Network Appliance(VNA) State | no instances in lab |
| `/infra/sites/{site-id}/napp/deployment/platform/checks/status` | Get NSX Application Platform pre/post checks progress status | HTTP 404x1 |
| `/infra/sites/{site-id}/napp/deployment/platform/status` | Get platform deployment or undeployment progress status | ✅ data (1 calls) |
| `/infra/sites/{site-id}/napp/deployment/upgrade-coordinator/checks/status` | Get NSX Application Platform upgrade-coordinator pre/post checks progress status. | ✅ data (1 calls) |
| `/infra/sites/{site-id}/napp/deployment/upgrade-coordinator/status` | Get deployment or undeployment progress status | ✅ data (1 calls) |
| `/infra/tags/tag-operations/{operation-id}/status` | Get status of tag bulk operation | no instances in lab |
| `/infra/third-party-ipam-providers/{provider-instance-id}/connection-status` | Read a third party IPAM provider connection status | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/arp-proxies` | Get Tier-0 Address Resolution Protocol Proxies | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/arp-proxies?format=csv` | Get Tier-0 Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-0s/{tier-0-id}/dns-forwarder/statistics` | Get tier-0 DNS forwarder statistics | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/dns-forwarder/status` | Get current status of tier-0 DNS forwarder | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/forwarding-table` | Get forwarding table from tier-0 | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/forwarding-table?format=csv` | Get forwarding table from tier-0 in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-0s/{tier-0-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/detailed-status` | Get IPSec VPN session detailed status under Tier-0 | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/statistics` | Get IPSec VPN session statistics under Tier-0 | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/ipsec-vpn-services/{service-id}/summary` | Get IPSec VPN Session Summary | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/l2vpn-services/{service-id}/sessions/{session-id}/detailed-status` | Get L2VPN session detailed status under Tier-0 | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/l2vpn-services/{service-id}/sessions/{session-id}/statistics` | Get L2VPN session statistics under Tier-0 | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp` | Read BGP routing config | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp/neighbors` | List BGP neighbor configurations | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp/neighbors/status` | Get BGP neighbor status for the Tier0 | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interface-groups/{interface-group-id}/statistics` | Get tier-0 interface group statistics information | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy` | Get Tier-0 Interface Address Resolution Protocol Proxies | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy?format=csv` | Get Tier-0 Interface Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table` | Get ARP table from tier-0 interface | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table?format=csv` | Get ARP table from tier-0 interface in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/dad-state` | Get DAD status by interface | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics` | Get tier-0 interface statistics information | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics/summary` | Get tier-0 interface statistics summary information | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/ospf/neighbors` | Get OSPF neighbor information | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/service-instances/{service-instance-id}/statistics` | Get statistics for all runtimes associated with this PolicyServiceInstance | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-svc-id}/tunnels/{tunnel-id}/statistics` | Get policy Tunnel(GRE as of now) statistics for given tunnel-id | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-svc-id}/tunnels/{tunnel-id}/statistics/summary` | Get policy Tunnel(GRE as of now) statistics summary for given tunnel-id | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/locale-services/{locale-svc-id}/tunnels/{tunnel-id}/status` | Get policy Tunnel(GRE as of now) status for given tunnel-id | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/nat/statistics` | List NAT Rules Statistics | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/nat/{nat-id}/nat-rules/{nat-rule-id}/statistics` | Get NAT Rule Statistics | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/routing-table` | Get routing table from tier-0 | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/routing-table?format=csv` | Get routing table from tier-0 in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-0s/{tier-0-id}/state` | Get Tier0 state | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/static-routes/bfd-peers` | List StaticRouteBfdPeers | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/static-routes/bfd-peers/{bfd-peer-id}` | Read a StaticRouteBfdPeer | no instances in lab |
| `/infra/tier-0s/{tier-0-id}/tier-1-interface/arp-table` | Get tier-0 router link arp information | skipped (required query parameter) |
| `/infra/tier-0s/{tier-0-id}/tier-1-interface/arp-table?format=csv` | Get ARP table from tier-0 router link interface in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-0s/{tier-0-id}/tier-1-interface/statistics` | Get tier-0 router link statistics information | skipped (required query parameter) |
| `/infra/tier-0s/{tier-0-id}/tier-1-interface/statistics/summary` | Get tier-0 router link statistics summary information | skipped (required query parameter) |
| `/infra/tier-0s/{tier-0-id}/tls-inspection-state` | TLS inspection execution state details for the tier0 | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/arp-proxies` | Get Tier-1 Address Resolution Protocol Proxies | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/arp-proxies?format=csv` | Get Tier-1 Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/dns-forwarder/statistics` | Get tier-1 DNS forwarder statistics | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/dns-forwarder/status` | Get current status of tier-1 DNS forwarder | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/forwarding-table` | Get forwarding table from tier-1 | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/forwarding-table?format=csv` | Get forwarding table from tier-1 in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/detailed-status` | Get IPSec VPN session detailed status under Tier-1 | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/statistics` | Get IPSec VPN session statistics under Tier-1 | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/ipsec-vpn-services/{service-id}/summary` | Get IPSec VPN Session Summary | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/l2vpn-services/{service-id}/sessions/{session-id}/detailed-status` | Get L2VPN session detailed status under Tier-1 | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/l2vpn-services/{service-id}/sessions/{session-id}/statistics` | Get L2VPN session statistics under Tier-1 | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interface-groups/{interface-group-id}/statistics` | Get tier-1 interface group statistics information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy` | Get Tier-1 Interface Address Resolution Protocol Proxies | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy?format=csv` | Get Tier-1 Interface Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table` | Get ARP table from tier-1 interface | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table?format=csv` | Get ARP table from tier-1 interface in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/dad-state` | Get DAD status by interface | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics` | Get tier-1 interface statistics information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics/summary` | Get tier-1 interface statistics summary information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/service-instances/{service-instance-id}/statistics` | Get statistics for all runtimes associated with this Tier1 PolicyServiceInstance | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/nat/statistics` | List NAT Rules Statistics | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules/{nat-rule-id}/statistics` | Get NAT Rule Statistics | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/state` | Get tier-1 segments by configuration state | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-proxy` | Get downlink port Address Resolution Protocol Proxies for tier-1 segment | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-proxy?format=csv` | Get downlink port Address Resolution Protocol Proxies for tier-1 segment in CSV | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-table` | Get ARP table from segment interface (downlink) | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-table?format=csv` | Get ARP table from segment interface (downlink) in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/bep-statistics` | Get Tier-1 segment bridge end point statistics using segment ID and profile path. | skipped (required query parameter) |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/bep-status` | Get Tier-1 segment bridge end point status using segment ID and profile path. | skipped (required query parameter) |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/dhcp-static-bindings/{binding-id}/state` | Read DHCP static binding state | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-dad-state` | Get DAD state for downlink router port on tier-1 router | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-statistics` | Get statistics for downlink router port on tier-1 router | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-statistics/summary` | Get statistics for downlink router port on tier-1 router | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/mac-table` | Get Tier-1 segment MAC table | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/mac-table?format=csv` | Get Tier-1 segment MAC table in CSV | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/mac-table` | Get MAC table for tier-1 segment port | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/mac-table?format=csv` | Get tier-1 segment port MAC table in CSV | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/port-monitoring-profile-binding-maps/{port-monitoring-profile-binding-map-id}/mirror-stack-status` | Get mirror stack status for Port Monitoring Profile Binding Map | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/state` | Get tier-1  segment port state | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/segment-monitoring-profile-binding-maps/{segment-monitoring-profile-binding-map-id}/mirror-stack-status` | Get mirror stack status for Segment Monitoring Profile Binding Map | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segment-id}/static-arp` | Read static ARP config | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segments-id}/ports/{port-id}/statistics` | Get tier-1 segment port statistics information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segments-id}/ports/{port-id}/status` | Get segment port status information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segments-id}/state` | Get segment state information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/segments/{segments-id}/statistics` | Get segment statistics information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/state` | Get Tier1 state | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/tier-0-interface/arp-table` | Get tier-1 router link arp information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/tier-0-interface/arp-table?format=csv` | Get ARP table from tier-1 router link interface in CSV format | skipped (excluded (download/blob)) |
| `/infra/tier-1s/{tier-1-id}/tier-0-interface/statistics` | Get tier-1 router link statistics information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/tier-0-interface/statistics/summary` | Get tier-1 router link statistics summary information | no instances in lab |
| `/infra/tier-1s/{tier-1-id}/tls-inspection-state` | TLS inspection execution state details for the tier1 | no instances in lab |
| `/infra/traceflows/{traceflow-id}/status` | Read traceflow status | no instances in lab |

### `licenses`

| Endpoint | Description | Lab result |
|---|---|---|
| `/licenses/action/async-query/status` | Get status of asynchronous query operation | HTTP 400x1 |
| `/licenses/vcf/action/async/status` | Get status of asynchronous query operation | HTTP 400x1 |

### `malware-prevention`

| Endpoint | Description | Lab result |
|---|---|---|
| `/malware-prevention/compute-collection/{compute-collection-id}/status` | Get status for MPS Compute collection. | no instances in lab |
| `/malware-prevention/teaser/status` | Registration status | ✅ data (1 calls) |
| `/malware-prevention/transport-node/{transport-node-id}/status` | Get status for MPS Transport Node. | no instances in lab |

### `management-plane-health`

| Endpoint | Description | Lab result |
|---|---|---|
| `/management-plane-health` | Get health stats for policy and the dependent services. | HTTP 403x1 |

### `orgs/projects (multi-tenancy / VPC)`

| Endpoint | Description | Lab result |
|---|---|---|
| `/orgs/{org-id}/projects/{project-id}/infra/dhcp-server-configs/{config-id}/state` | Read DHCP server state | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/infra/dhcp-server-configs/{config-id}/stats` | Read DHCP server statistics | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/infra/dhcp-server-configs/{config-id}/status` | Read DHCP server status | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/infra/domains/{domain-id}/gateway-policies/{gateway-policy-id}/rules/{rule-id}/statistics` | Get gateway rule statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/domains/{domain-id}/gateway-policies/{gateway-policy-id}/statistics` | Get gateway policy statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/domains/{domain-id}/intrusion-service-policies/{ids-policy-id}/rules/{rule-id}/statistics` | Get IDS-IPS rule statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/domains/{domain-id}/intrusion-service-policies/{ids-policy-id}/statistics` | Get IDS security policy statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/domains/{domain-id}/security-policies/{security-policy-id}/rules/{rule-id}/statistics` | Get rule statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/domains/{domain-id}/security-policies/{security-policy-id}/statistics` | Get security policy statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/ip-blocks/allocation-state` | IpAddressBlocks allocation states | HTTP 405x1 |
| `/orgs/{org-id}/projects/{project-id}/infra/ip-blocks/state` | Get state of the given IpAddressBlock | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/infra/ip-blocks/usage` | Usage Details for all IpAddressBlocks | HTTP 405x1 |
| `/orgs/{org-id}/projects/{project-id}/infra/ip-blocks/{ip-block-id}/allocation-state` | IpAddressBlock allocation state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/ip-blocks/{ip-block-id}/usage` | Get an IpAddressBlock usage | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/limits/state` | Get consumption details and other operational state for limits | HTTP 405x1 |
| `/orgs/{org-id}/projects/{project-id}/infra/limits/{limit-id}/state` | Get consumption details and other operational state for a limit | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/realized-state/realized-entities` | Get list of realized objects associated with intent object | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/infra/realized-state/status` | Get consolidated status of an intent object | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/state` | Get infra segments by configuration state | HTTP 405x1 |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/arp-proxy` | Get downlink port Address Resolution Protocol Proxies for infra segment | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/arp-proxy?format=csv` | Get downlink port Address Resolution Protocol Proxies for infra segment in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/arp-table` | Get ARP table from segment interface (downlink) | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/arp-table?format=csv` | Get ARP table from segment interface (downlink) in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/dhcp-static-bindings/{binding-id}/state` | Read DHCP static binding state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/gateway-interface-dad-state` | Get DAD state for downlink router port on tier-0 router | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/gateway-interface-statistics` | Get statistics for downlink router port on tier-0 router | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/gateway-interface-statistics/summary` | Get statistics for downlink router port on tier-0 router | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/mac-table` | Get infra segment MAC table | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/mac-table?format=csv` | Get infra segment MAC table in CSV | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/ports/{port-id}/mac-table` | Get MAC table for infra segment port | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/ports/{port-id}/mac-table?format=csv` | Get infra segment port MAC table in CSV | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segment-id}/ports/{port-id}/state` | Get infra segment port state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segments-id}/ports/{port-id}/statistics` | Get infra segment port statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segments-id}/ports/{port-id}/status` | Get infra segment port status information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segments-id}/state` | Get infra segment state information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/segments/{segments-id}/statistics` | Get infra segment statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/sites/agents/metrics` | Fetch current Metric agent config | HTTP 405x1 |
| `/orgs/{org-id}/projects/{project-id}/infra/tags/tag-operations/{operation-id}/status` | Get status of tag bulk operation | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-0s/{tier-0-id}/ipsec-vpn-services/{service-id}/summary` | Get IPSec VPN Session Summary | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/arp-proxies` | Get Tier-1 Address Resolution Protocol Proxies | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/arp-proxies?format=csv` | Get Tier-1 Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/dns-forwarder/statistics` | Get tier-1 DNS forwarder statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/dns-forwarder/status` | Get current status of tier-1 DNS forwarder | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/forwarding-table` | Get forwarding table from tier-1 | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/forwarding-table?format=csv` | Get forwarding table from tier-1 in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/detailed-status` | Get IPSec VPN session detailed status under Tier-1 | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/statistics` | Get IPSec VPN session statistics under Tier-1 | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/ipsec-vpn-services/{service-id}/summary` | Get IPSec VPN Session Summary | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/l2vpn-services/{service-id}/sessions/{session-id}/detailed-status` | Get L2VPN session detailed status under Tier-1 | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/l2vpn-services/{service-id}/sessions/{session-id}/statistics` | Get L2VPN session statistics under Tier-1 | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interface-groups/{interface-group-id}/statistics` | Get tier-1 interface group statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy` | Get Tier-1 Interface Address Resolution Protocol Proxies | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-proxy?format=csv` | Get Tier-1 Interface Address Resolution Protocol Proxies in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table` | Get ARP table from tier-1 interface | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/arp-table?format=csv` | Get ARP table from tier-1 interface in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/dad-state` | Get DAD status by interface | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics` | Get tier-1 interface statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/locale-services/{locale-service-id}/interfaces/{interface-id}/statistics/summary` | Get tier-1 interface statistics summary information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/nat/statistics` | List NAT Rules Statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules/{nat-rule-id}/statistics` | Get NAT Rule Statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/state` | Get tier-1 segments by configuration state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-proxy` | Get downlink port Address Resolution Protocol Proxies for tier-1 segment | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-proxy?format=csv` | Get downlink port Address Resolution Protocol Proxies for tier-1 segment in CSV | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-table` | Get ARP table from segment interface (downlink) | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/arp-table?format=csv` | Get ARP table from segment interface (downlink) in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/dhcp-static-bindings/{binding-id}/state` | Read DHCP static binding state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-dad-state` | Get DAD state for downlink router port on tier-1 router | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-statistics` | Get statistics for downlink router port on tier-1 router | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/gateway-interface-statistics/summary` | Get statistics for downlink router port on tier-1 router | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/mac-table` | Get Tier-1 segment MAC table | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/mac-table?format=csv` | Get Tier-1 segment MAC table in CSV | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/mac-table` | Get MAC table for tier-1 segment port | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/mac-table?format=csv` | Get tier-1 segment port MAC table in CSV | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/ports/{port-id}/state` | Get tier-1  segment port state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segment-id}/static-arp` | Read static ARP config | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segments-id}/ports/{port-id}/statistics` | Get tier-1 segment port statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segments-id}/ports/{port-id}/status` | Get segment port status information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segments-id}/state` | Get segment state information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/segments/{segments-id}/statistics` | Get segment statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/state` | Get Tier1 state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/tier-0-interface/arp-table` | Get tier-1 router link arp information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/tier-0-interface/arp-table?format=csv` | Get ARP table from tier-1 router link interface in CSV format | skipped (excluded (download/blob)) |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/tier-0-interface/statistics` | Get tier-1 router link statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/tier-1s/{tier-1-id}/tier-0-interface/statistics/summary` | Get tier-1 router link statistics summary information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/infra/traceflows/{traceflow-id}/status` | Read traceflow status | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/lb-node-capacity-status` | Get LB node capacity | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/limits/state` | Get consumption details and another operational state for limits for VPCs within a project | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/quota-stats` | Get quota details | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/state` | Get Project state | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/arp-proxies` | Get Transit Gateway Address Resolution Protocol Proxies | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/attachments/{attachment-id}/state/interfaces/{interface-id}/statistics` | Get per node statistics for transit gateway attachment interfaces. | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/attachments/{attachment-id}/statistics` | Get transit gateway attachment statistics. | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/forwarding-table` | Get forwarding table from TGW | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/detailed-status` | Get IPSec VPN session detailed status under Transit Gateway | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/ipsec-vpn-services/{service-id}/sessions/{session-id}/statistics` | Get IPSec VPN session statistics under Transit Gateway | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/ipsec-vpn-services/{service-id}/summary` | Get IPSec VPN Session Summary | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/nat/statistics` | List NAT Rules Statistics | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/nat/{nat-id}/nat-rules/{nat-rule-id}/statistics` | Get transit gateway NAT Rule Statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/routing-table` | Get routing table from TGW | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/state` | Get Transit Gateway state | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/statistics` | Get Transit Gateway statistics | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/transit-gateways/{transit-gateway-id}/status` | Get current status of TGW | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/vc-folder-status` | VC Folder Status for Project | ✅ data (1 calls) |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/arp-proxies` | Get VPC Address Resolution Protocol proxies | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/dns-forwarder-statistics` | Get DNS Forwarder statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/forwarding-table` | Get forwarding table from VPC | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/gateway-policies/{gateway-policy-id}/rules/{rule-id}/statistics` | Get rule statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/gateway-policies/{gateway-policy-id}/statistics` | Get gateway policy statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/ip-address-usage` | Get ip address usage for vpc | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/ip-blocks/allocation-state` | VPC IpAddressBloock Allocation State | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/ip-blocks/usage` | IpAddressBlock usage for VPC | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/limits/state` | Get consumption details and other operational state for limits for a VPC | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/nat/statistics` | List NAT Rules Statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/nat/{nat-id}/nat-rules/{nat-rule-id}/statistics` | Get NAT Rule Statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/quota-stats` | Get quota details | skipped (required query parameter) |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/security-policies/{security-policy-id}/rules/{rule-id}/statistics` | Get rule statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/security-policies/{security-policy-id}/statistics` | Get security policy statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/state` | Get VPC state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/statistics` | Get VPC Statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/statistics/summary` | Get VPC Statistics Summary | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/status` | Get VPC Status | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/arp-proxy` | Get downlink port Address Resolution Protocol Proxy for VPC subnet | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/arp-table` | Get ARP table from VPC subnet (downlink) | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/dhcp-server-config/stats` | Read VPC Subnet DHCP server statistics | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/dhcp-server-config/status` | Read Vpc Subnet DHCP server status | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/mac-table` | Get VPC subnet MAC table | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/ports/{port-id}/mac-table` | Get MAC table for VPC Subnet port | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/ports/{port-id}/state` | Get VPC Subnet port state | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/ports/{port-id}/statistics` | Get Vpc subnet port statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/ports/{port-id}/status` | Get Vpc subnet port status information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/state` | Get Vpc Subnet state information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/statistics` | Get VPC Subnet statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/subnets/{subnet-id}/status` | Get VPC Subnet status | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/tags/vpc-tag-operations/{operation-id}/status` | Get status of tag bulk operation | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vc-folder-status` | VC Folder Status for Vpc | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lb-node-capacity-status` | Get LB node capacity | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lbs/{vpc-lb-id}/detailed-status` | Get load balancer status information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lbs/{vpc-lb-id}/statistics` | Get load balancer statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lbs/{vpc-lb-id}/usage` | Get load balancer usage information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lbs/{vpc-lb-id}/vpc-lb-pools/{vpc-lb-pool-id}/detailed-status` | Get LBPool status information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lbs/{vpc-lb-id}/vpc-lb-pools/{vpc-lb-pool-id}/statistics` | Get LBPool statistics information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lbs/{vpc-lb-id}/vpc-lb-virtual-servers/{vpc-lb-virtual-server-id}/detailed-status` | Get LBVirtualServer status information | no instances in lab |
| `/orgs/{org-id}/projects/{project-id}/vpcs/{vpc-id}/vpc-lbs/{vpc-lb-id}/vpc-lb-virtual-servers/{vpc-lb-virtual-server-id}/statistics` | Get LBVirtualServer statistics information | no instances in lab |

### `search`

| Endpoint | Description | Lab result |
|---|---|---|
| `/search/reconcile/status` | API to get the search reconciliation status | ✅ data (1 calls) |
