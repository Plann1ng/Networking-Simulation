---
# README.md

## 🔧 Project: Network Automation with Ansible on Ubuntu

### 🖥️ Host Environment
This automation is configured and run from an **Ubuntu Linux** machine using **Ansible**. It is designed to push syslog configurations to Cisco routers and switches, and also forms the basis for future security-triggered automation involving Cisco ASA firewalls.

---

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
          ansible_host: 10.10.10.1
          ansible_user: admin
          ansible_password: admin123
    switches:
      hosts:
        switch1:
          ansible_host: 10.10.10.2
          ansible_user: admin
          ansible_password: admin123
```

---

## ✅ Step 3: Playbook to Push Syslog Settings (syslog_config.yml)

```yaml
- name: Push syslog config to Cisco devices
  hosts: all
  gather_facts: no
  connection: network_cli

  tasks:
    - name: Configure syslog server
      ios_config:
        lines:
          - logging host 10.10.10.98
          - logging trap informational
```

---

## 🔜 Future Plans: ASA-triggered Shutdown via Ansible

This setup will later be expanded to include:
- **Cisco ASA** logs forwarded to **Splunk**.
- **Real-time Splunk alerts** for blacklisted access attempts.
- A trigger to run Ansible to shutdown the interface on the router/switch that connects the offending device.

---

## 🚀 To Run
```bash
ANSIBLE_INVENTORY_ENABLED=ini,yaml ansible-playbook -i hosts.yml syslog_config.yml
```

---

Feel free to fork this repo and enhance it for NMS, SNMP, backup automation, or security enforcement policies.
