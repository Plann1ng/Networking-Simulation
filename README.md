# Networking-Simulation
# Enterprise-Grade Network Security Lab (GNS3 + ISE + WLC + AD + Splunk)

This lab simulates a full enterprise-grade network infrastructure using GNS3. It includes VLAN segmentation, Cisco ISE for wired/wireless 802.1X authentication, Active Directory (DNS, DHCP, NTP, SNMP), Splunk for centralized logging, and simulated wireless using hostapd or Cisco vWLC. A VPN gateway is also planned to be implemented for remote access simulation.

> 💡 This lab is deployed and tested on **GNS3 running on Linux (Kali)**. The Splunk server is hosted on an **Ubuntu VM inside Virtual Machine Manager (virt-manager)**. The Ubuntu VM uses a **bridged interface** to get internet access and participate in the GNS3 virtual network.

## 🎯 Lab Goals

* Simulate realistic enterprise network infrastructure
* Implement Cisco ISE for 802.1X authentication and dynamic VLAN assignment
* Integrate wireless access using hostapd or vWLC with ISE policies
* Deploy VPN gateway to simulate secure remote access
* Centralize logging using Splunk
* Practice switch, router, and firewall configurations

---

## 🧱 Components

| Component      | Role/Function                                 |
| -------------- | --------------------------------------------- |
| GNS3           | Core network simulation platform (Linux host) |
| Cisco Routers  | Core layer with HSRP + OSPF                   |
| L3 Switches    | VLANs, SVIs, DHCP relays                      |
| Cisco ISE      | 802.1X, MAB, NAC, dynamic VLAN assignment     |
| Windows Server | AD, DNS, DHCP, NTP, SNMP                      |
| Splunk         | Syslog and ISE log ingestion (on Ubuntu VM)   |
| hostapd/vWLC   | Wireless LAN Controller + simulated SSIDs     |
| VPN Gateway    | Secure remote access endpoint (planned)       |
| Client VMs     | Windows/Linux (802.1X and web auth testing)   |

---

## 🗺️ Network Design

### VLAN Plan:

| VLAN | Name           | Subnet        | Purpose               |
| ---- | -------------- | ------------- | --------------------- |
| 10   | Users          | 10.10.10.0/24 | Authenticated Clients |
| 20   | Guests         | 10.20.20.0/24 | MAB/Guest VLAN        |
| 30   | Security Ops   | 10.30.30.0/24 | Splunk & Admin PCs    |
| 40   | Infrastructure | 10.40.40.0/24 | AD, ISE, DHCP, DNS    |
| 50   | Wireless Mgmt  | 10.50.50.0/24 | vWLC, Wireless APs    |

---

## 🔧 Setup Steps (Chronological)

### 1. Planning

* Create detailed IP and VLAN assignments
* Design physical and logical topology

### 2. Install GNS3 on Kali Linux (Challenges Noted Below)

* Install GNS3 and dependencies manually
* Configure `gns3server` to run independently
* Ensure proper permissions for Wireshark and QEMU

### 3. Bridge Network Interfaces

* Create and configure `br0` for LAN integration
* Add `tap0` with appropriate bridge and routing rules
* Ensure both interfaces persist across reboots

### 4. Deploy Base Servers

* **Windows Server**: Install AD, DHCP, DNS, NTP
* **Splunk Server**: Install Splunk Enterprise (Ubuntu VM inside virt-manager)
* Configure DHCP scopes per VLAN

### 5. Network Layer

* Set up GNS3 routers with HSRP between core routers
* Deploy L3 switches with SVIs and `ip routing`
* Trunk ports between switches and routers
* Add DHCP relays:

  ```bash
  interface vlan 10
   ip helper-address 10.40.40.2
  ```

### 6. Cisco ISE

* Deploy ISE (QEMU or VMware)
* Configure basic setup: IP, hostname, DNS, NTP
* Add network devices (switches, WLC)
* Define authentication and authorization policies
* Enable internal CA (optional)

### 7. 802.1X on Switches

```bash
aaa new-model
radius-server host 10.40.40.3 key ISE_SECRET
ip radius source-interface vlan 40
!
dot1x system-auth-control
!
interface FastEthernet0/1
 switchport mode access
 authentication port-control auto
 dot1x pae authenticator
 spanning-tree portfast
```

### 8. Wireless Setup (Choose One)

#### Option A: hostapd (Open Source)

* Run `hostapd` on Linux VM with USB Wi-Fi or bridge
* Connect clients to WPA2-Enterprise SSID
* Point to ISE via FreeRADIUS or raw RADIUS config

#### Option B: Cisco vWLC + Lightweight AP

* Deploy vWLC in VLAN 50
* Connect AP via trunk link
* Configure WLAN → use RADIUS auth with ISE
* Create client SSID (802.1X enabled)

### 9. Logging (Splunk)

* Enable syslog on switches:

```bash
logging host 10.30.30.2
logging trap informational
```

* Forward ISE syslogs to Splunk (UDP 514)
* Optional: Create dashboards for auth events

### 10. Testing

* Connect client VM to access port
* Trigger MAB/802.1X auth via switch
* Check ISE logs and Splunk events
* Validate VLAN assignment and network access

---

## ⚠️ Setup Challenges & Fixes

* **GNS3 on Kali**: Required manual installation and fixing broken dependencies.
* **gns3server must be launched manually** before starting the GUI or project.
* **Network bridging**: Setting up `br0` and `tap0` interfaces with persistent NAT/bridge configs was non-trivial.
* **Permissions**: Had to manually allow user access to Wireshark/QEMU network interfaces.

---

## 🔍 Reasoning Behind Design Choices

* **GNS3 on Linux**: Offers strong support for virtualization, better resource handling for ISE and vWLC, and native integration with virt-manager.
* **Bridged Interface for Splunk VM**: Ensures connectivity with both the simulated GNS3 network and external resources like updates or syslog collection.
* **Cisco ISE**: Allows centralized identity-based policy enforcement using RADIUS, 802.1X, and MAB for both wired and wireless clients.
* **Wireless Simulation**: Covers real-world enterprise use cases with either cost-free hostapd or Cisco-standard vWLC/AP deployments.
* **Splunk Logging**: Centralized monitoring solution for correlating authentication events, rogue device activity, and system health.
* **Dynamic VLANs**: Supports segmentation based on user or device role, enforced via ISE policies.
* **VPN Gateway (Planned)**: Enables remote access simulation for workforce or red-team testing in a zero-trust model.

---

## 📂 Additional Files

All device configuration files (switches, routers, ISE, WLC, VPN) will be provided in a separate `/configs` directory inside this repository. These include:

* Layer 3 switch and trunk configs
* DHCP relay setups
* HSRP/OSPF router configs
* ISE network device profiles and policies
* vWLC WLAN and RADIUS configs
* VPN configuration (OpenVPN or Cisco VPN setup, TBD)
