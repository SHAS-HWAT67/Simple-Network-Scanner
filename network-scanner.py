#import scapy 
import scapy.all as scapy 

#ARP() is function defined in scapy module which allows us to create ARP packets (request or response)
#By default, if we are calling it, it will create an ARP request packet for us.

request = scapy.ARP() 

#show() gives detailed information about the packet
print(request.show())

#ls() gives what are the fields that we can set for a specific packet
print(scapy.ls(scapy.ARP()))
