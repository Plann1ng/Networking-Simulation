# 📘 Windows Server (AD, DNS, DHCP, NTP) - README.md

## 🎯 Purpose

This Windows Server acts as the **central identity, time, and infrastructure authority** in the lab. It is a domain controller (`gns3.lab`) and is fully integrated with ISE and other systems.

## 🔐 AD Integration with Cisco ISE

* Cisco ISE is **joined to the Active Directory domain** `gns3.lab`
* ISE uses AD to authenticate users during 802.1X login via RADIUS
* AD groups are mapped to **authorization policies** in ISE
* Test accounts (e.g., `student01`, `admin01`) were created and joined to AD
* **Posture validation and group-based dACLs** are assigned based on user group membership

## 📡 DNS, DHCP, and NTP

* **DNS**: Used for ISE profiling, including dynamic resolution of hostnames (e.g., `WIN7-PC1.gns3.lab`)
* **DHCP**: Windows Server provides IP addresses to Windows 7 clients; ISE listens to DHCP traffic for profiling
* **NTP**: All devices, including ISE and routers, are time-synced to avoid RADIUS/Kerberos failures

## 🔍 Profiling Use Case

* Windows 7 endpoints were dynamically profiled based on:

  * DHCP attributes
  * DNS lookups
  * NetBIOS name
* ISE shows detailed visibility into whether clients have antivirus, OS versions, and domain join status
