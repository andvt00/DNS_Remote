#!/usr/bin/env python3
from scapy.all import*
# Construct the DNS header and payload
Qdsec  = DNSQR(qname='duong.example.com')
dns    = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0,arcount=0, qd=Qdsec)
# Construct the IP, UDP headers, and the entire packet
ip  = IP(dst='10.9.0.5', src='192.168.1.6')
udp = UDP(dport=40000, sport=33333, chksum=0)
request = ip/udp/dns
# Save the packet to a file
with open('ip_req.bin', 'wb') as f:
    f.write(bytes(request))
