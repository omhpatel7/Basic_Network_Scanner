# Network Scanner

This Python script scans a local network for connected devices, identifying their IP addresses, MAC addresses, and hostnames.

## Requirements

- Python 3.x
- [Scapy](https://scapy.net/) library

## Installation

First, ensure you have Python installed on your system. Then, you can install the required library using `pip`:

```sh
pip install scapy
```

## Usage
1. Clone this repository or download the script.
2. Run the script using Python:
```sh
python scanner.py
```

The script will scan the specified IP address range and list the devices found on the network along with their hostnames, IP addresses, and MAC addresses.

## Script Overview
The script performs the following steps:

1. **Set the Target IP Range**: Define the IP address range to scan.
```sh
targe = "192.168.50.1/24" # IP Address range to scan
```
2. **Create ARP and Ethernet Packets**: Construct the ARP and Ethernet packets to broadcast on the network.
```sh
arp_packet = ARP(pdst=target)
ether_packet = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether_packet / arp_packet
```
3. **Send Packets and Receive Responses**: Use Scapy to send the packet and capture responses from devices.
```sh
res = srp(packet, timeout=3, verbose=0)[0]
```
4. **Parse the Responses**: Extract IP and MAC addresses from the responses and resolve the IP address to a hostname.
```sh
clist = []
for _, rcv in res:
    ip = rcv.psrc
    mac = rcv.hwsrc
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "Unknown"
    clist.append({'ip': ip, 'mac': mac, 'hostname': hostname})
```
5. **Display the Results**: Print the list of devices found on the network.
```sh
print("Devices in Network")
print("Hostname" + " " * 12 + "IP" + " " * 18 + "MAC")
for client in clist:
    print("{:16} {:16} {}".format(client['hostname'], client['ip'], client['mac']))
```

## Example Output
```sh
Devices in Network
Hostname        IP                MAC
Unknown         192.168.50.2      00:11:22:33:44:55
Unknown         192.168.50.3      66:77:88:99:aa:bb
MyDevice        192.168.50.4      cc:dd:ee:ff:00:11
```

## License
This project is licensed under the MIT License.
