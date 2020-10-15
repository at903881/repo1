import logging
import socket
from scapy.all import *
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys

def print_summary(pkt):
    if IP in pkt:
        ip_src=pkt[IP].src
        ip_dst=pkt[IP].dst
    if TCP in pkt:
        tcp_sport=pkt[TCP].sport
        tcp_dport=pkt[TCP].dport

        print(" IP src " + str(ip_src) + " TCP sport " + str(tcp_sport)) 
        print(" IP dst " + str(ip_dst) + " TCP dport " + str(tcp_dport))

    # filtering with specific IP
    #if ( ( pkt[IP].src == "192.168.0.1") or ( pkt[IP].dst == "192.168.0.1") ):
        #print("!")

if len(sys.argv)!=4:
    print("Usage: %s target startport endport" %(sys.argv[0]))
    sys.exit(0)
target = str(sys.argv[1])
startport = int(sys.argv[2])
endport = int(sys.argv[3])
print("Scanning "+target+" for open TCP ports\n")

if startport==endport:
    endport+=1
for x in range(startport,endport):
    packet = IP(dst=target)/TCP(dport=x, flags='S')
    response = sr1(packet, timeout=0.5, verbose=0)
    if response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:   
        print('Port '+str(x)+' OPEN'+" service name: %s" %(socket.getservbyport(x, "tcp")))
        sniff(filter='port {}'.format(x), count=1, timeout=10, prn=print_summary)
        print()
        sniff(filter='port {}'.format(x), count=1, timeout=10, prn=lambda x:x.summary)
    sr(IP(dst=target)/TCP(dport=response.sport,flags='R'), timeout=0.5,verbose=0)
print("\nScan is complete")
    
