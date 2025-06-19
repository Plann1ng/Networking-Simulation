---
# README.md

## 🔧 Project: Network Automation with Ansible on Ubuntu

### 🖥️ Host Environment
This automation is configured and run from an **Ubuntu Linux** machine using **Ansible**. It is designed to push syslog configurations to Cisco routers and switches, it can also be used as a skeleton to push any other type of configurations to the registered hosts.

---

## Prerequisites (Ubuntu based host with Cisco IOS devices):
1. Python3 library on Ubuntu machine
2. Enable SSH on the host machines (Since this is a lab setup this config uses same password for all the hosts, however consider using different password for each device within your network.)



## ✅ Step 1: Install Ansible on Ubuntu

Official guide: [Installing Ansible on Ubuntu](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

Quick commands:
```bash
sudo apt update
sudo apt install -y python3-pip
pip install ansible
```

To confirm installation:
```bash
ansible --version
```


---

## ✅ Step 2: Inventory File (hosts.yml)

```yaml
all:
  children:
    routers:
      hosts:
        router1:
          SpineRouter1: 10.10.10.1
          ansible_user: admin
          ansible_password: admin123
    switches:
      hosts:
        LeafSwitch1:
          ansible_host: 10.10.10.2
          ansible_user: admin
          ansible_password: admin123
```

---

## ✅ Step 3: Playbook to Push Syslog Settings (base_config.yml)

```yaml
- name: Push syslog, NTP, and SNMP config to Cisco devices
  hosts: all
  gather_facts: no
  connection: network_cli

  tasks:
    - name: Configure syslog server
      ios_config:
        lines:
          - logging host 10.10.10.98
          - logging trap informational

    - name: Configure NTP server
      ios_config:
        lines:
          - ntp server 10.10.10.102
          - clock timezone UTC 0

    - name: Configure SNMP server
      ios_config:
        lines:
          - snmp-server community public RO
          - snmp-server location Lab-Network
          - snmp-server contact admin@gns3lab.com
          - snmp-server host 10.10.10.102 version 2c public

```

---

## 🔜 Future Plans: SSH Brute Force Detection + Automated Port Shutdown

(Considering the intruder is within the VLAN and he is a current employee with unethical intentions)

Syslog-based monitoring of SSH login attempts from Cisco devices.
Splunk detects repeated failed login attempts (e.g., 3+ within 2 minutes).
Splunk alert triggers Ansible, which locates the offending IP and shuts down the switch port using CDP/LLDP or ARP correlation.
Optional integration with Cisco ISE to enrich logs with device info like OS, hostname, and user context.

---

## 🚀 To Run
```bash
ANSIBLE_INVENTORY_ENABLED=ini,yaml ansible-playbook -i hosts.yml syslog_config.yml
```

---
