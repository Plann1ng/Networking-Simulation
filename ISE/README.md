
# 📘 Cisco ISE

## 🔐 Role in the Lab

Cisco ISE provides **identity-based access control**. It integrates with:

* AD for user validation
* DNS/DHCP for profiling
* RADIUS for authentication
* Splunk for monitoring (via syslog)

## 🧠 Realistic Use Cases

* **User connects** → dot1x request sent → ISE validates via AD
* Based on the **AD group**, user gets assigned a **dACL** or **VLAN**
* Windows 7 PC gets profiled → ISE checks if antivirus is present
* Failed authentications get **logged to Splunk**, triggering alerts

## 🛠️ Dynamic Access Control (dACL)

* Configured per policy
* Example:

  * Domain User → VLAN 10, full access
  * Guest → VLAN 20, restricted dACL

## ⚠️ Setup Notes

* Required increasing laptop RAM to **32 GB** to run ISE VM stably
* ISE required a minimum of **12 GB RAM + 4 vCPUs + 200 GB disk**

