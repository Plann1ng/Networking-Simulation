# 📘 Ubuntu Server (Splunk + Ansible)

## 🛠 Purpose

The Ubuntu VM acts as:

* **SIEM system** via Splunk
* **Network automation controller** via Ansible


## ⚙️ Ansible Automation

* Used to push:

  * NTP/DNS/SNMP settings
  * ACL changes (triggered via Splunk alerts)
  * Failover routing or interface shutdowns
  * Automated VLAN intrusion automation by collecting logs from internal hosts for unathorized access tries and triggering .sh script on the host machine where the intruder's mac adress is shunned from the switch by dynamic swithport security protect mechanism. Further collecting more information about the specific device through ISE regarding the username, OS and emailing the logs to the responsibles for further check.

## 🔍 Splunk Use Cases

* **Syslog ingestion** from routers, switches, ISE
* Alerts created for:

  * RADIUS failures
  * Interface state changes (using IP SLA tracking)
  * Excessive login failures or port scans
* Alerts can **trigger shell scripts** that run Ansible playbooks

