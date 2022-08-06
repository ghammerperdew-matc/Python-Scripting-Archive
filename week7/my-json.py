#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: analyzes an IP address using the ipinfo.io online API
"""

#imports

import json
import requests
import argparse
import sys



#create parser object

parser = argparse.ArgumentParser(description="")



#add --ipaddress argument

parser.add_argument("--ipaddress", dest="IP_ADDRESS", help="Enter an IP address to analyze")



#parse the args

args = parser.parse_args()



#if no args were passed, print help

if len(sys.argv) == 1:
    
    print(parser.print_help())

    exit(0)



#get content/response from webpage using ip address supplied in argument

jsonResponse = requests.get(f"http://ipinfo.io/{args.IP_ADDRESS}/json")



#convert json response to a dictionary

myDict = json.loads(jsonResponse.text)



#print key:value pairs from generated dictionary

for key in myDict.keys():

    print(f"{key}: {myDict[key]: >2}")

