from scapy.all import ARP, Ether, srp
import socket

target = "192.168.50.1/24"  # IP Address range to scan

# Create ARP packet
arp_packet = ARP(pdst=target)

# Create Ether packet
ether_packet = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine packets
packet = ether_packet / arp_packet

try:
    # Send packet and receive response
    res = srp(packet, timeout=3, verbose=0)[0]

    # List of clients
    clist = []

    # Iterate through responses
    for _, rcv in res:
        # Get IP and MAC address
        ip = rcv.psrc
        mac = rcv.hwsrc

        # Resolve IP address to hostname
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"

        # Append to client list
        clist.append({'ip': ip, 'mac': mac, 'hostname': hostname})

    # Print devices
    print("Devices in Network")
    print("Hostname" + " " * 12 + "IP" + " " * 18 + "MAC")
    for client in clist:
        print("{:16} {:16} {}".format(client['hostname'], client['ip'], client['mac']))

except Exception as e:
    print("An error occurred:", e)
