from scapy.all import *

#checks if packet has DNS layer, if yes, prints out IP source and destination and UDP and DNS protocols' fields
def query_sniff(pkt):
    if DNS in pkt:
        #if DNS request
        if pkt[DNS].qr == 0:
            print str(pkt[IP].src) + " -> " + str(pkt[IP].dst) + " : request to: " + pkt[DNS].qd.qname
            #makes sense to print out UDP header also, as we also need ports for spoofing
            pkt[UDP].show()
        else:
            print str(pkt[IP].src) + " -> " + str(pkt[IP].dst) + " : response from: " + pkt[DNS].an.rrname
            pkt[UDP].show()

#sniffs packets, filters out UDP ones and apply query_sniff() function to them
sniff(filter="port 53", prn=query_sniff)
