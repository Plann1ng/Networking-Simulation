# 📘 Ubuntu Server (Splunk + Ansible)

## 🛠 Purpose

The Ubuntu VM acts as:

* **SIEM system** via Splunk
* **Network automation controller** via Ansible

## 🔍 Splunk Use Cases

* **Syslog ingestion** from routers, switches, ISE
* Alerts created for:

  * RADIUS failures
  * Interface state changes (using IP SLA tracking)
  * Excessive login failures or port scans
* Alerts can **trigger shell scripts** that run Ansible playbooks

## ⚙️ Ansible Automation

* Used to push:

  * NTP/DNS/SNMP settings
  * ACL changes (triggered via Splunk alerts)
  * Failover routing or interface shutdowns
* Future plan: automate **interface shutdown** for unauthorized hosts detected by ISE or Splunk
