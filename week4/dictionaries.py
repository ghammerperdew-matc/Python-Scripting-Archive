#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: establishes a dictionary with domain names and ip addresses and performs operations on it.
"""


#create dictionary of FQDNs to IP addresses
domains = {
    "server1.testlab.com": "192.168.1.10",
    "server2.testlab.com": "192.168.1.11",
    "server3.testlab.com": "192.168.1.12",
    "server4.testlab.com": "192.168.1.13",
    "server5.testlab.com": "192.168.1.14",
    "server6.testlab.com": "192.168.1.15"
}

#list all FQDNs in the dictionary
print(f"\n\nHere are all of the FQDN's in the dictionary:\n{domains.keys()}\n\n")

#list all IP addresses in the dictionary
print(f"Here are all of the IP addresses in the dictionary:\n{domains.values()}\n\n")

#list all key/value pairs
print(f"Here are the FQDN's matched to their IP addresses:\n{domains.items()}\n\n")

#add server7 and server8 to the dictionary, continue IP sequence
domains["server7.testlab.com"] = "192.168.1.16"
domains["server8.testlab.com"] = "192.168.1.17"

#test if server2.testlab.com is contained in the dictionary
print("Does server2.testlab.com exist in the dictionary?")
if "server2.testlab.com" in domains:
    print("Yes it does!\n")
else:
    print("No it doesn't :(\n")

#test if server10.testlab.com is contained in the dictionary
print("Does server10.testlab.com exist in the dictionary?")
if "server10.testlab.com" in domains:
    print("Yes it does!\n")
else:
    print("No it doesn't :(\n")