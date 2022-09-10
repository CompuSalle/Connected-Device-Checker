from scapy.all import ARP, Ether, srp

ip_addr = "192.168.100.1/24"

detection_connected = ARP(pdst=ip_addr)

mac_addr = Ether(dst="ff:ff:ff:ff:ff:ff")

save_it = mac_addr/detection_connected

all_in = srp(save_it, timeout=3, verbose=0)[0]

users = []

for sent, found in all_in:
    users.append({'ip': found.psrc, 'mac': found.hwsrc})

# print clients
print("\n[+] Connected devices:\n")
print("-IP-" + " "*20+" -MAC-")
for connect in users:
    print("{:18}    {}".format(connect['ip'], connect['mac']))