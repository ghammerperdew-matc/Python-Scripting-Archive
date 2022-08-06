#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: Final exam
"""


#imports
import argparse
import requests
import sys
import bs4
import json
import socket



#############
##Functions##
#############

#Function 1
def get_response(website):
    
    #get content
    response = requests.get(website)
    
    return response.text


def parse_string(website):
    
    #get content from website
    response = requests.get(website)

    #parse content into single bs4 string without tags
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    headerTwo = soup.select("h2")[0].string

    #slice the string to reveal hidden message: "Found it!"
    message = headerTwo[7:32:3]

    return message


def parse_header(website):
    
    #get content from website
    response = requests.get(website)
    
    #all headers can be seen as a dictionary using response.headers
    message = response.headers["FINAL-HEADER"]
    
    return message


def parse_json(website):
    
    #get content from site
    response = requests.get(website)

    #convert json to dictionary that can be worked with
    jsonText = json.loads(response.text)

    #the top level dictionary has one key, and its value is a list
    #the list can be assigned to its own variable to make it easier to work with
    dictList = jsonText["Music And Books"]
    
    # 'item' represents the dictionaries in the list assigned to 'Music And Books'
    for item in dictList:

        #don't need another loop, just need to search each dictionary's values for desired value
        if "The Shining" in item.values():

            #publish year is in a nested dictionary, so double [] can access that
            pubYear = item["publish_info"]["publish_year"]

    return pubYear


def socket_client(ip_address):
    
    RHOST = ip_address
    SND_DATA = "secret"
    RCV_DATA = ""

    for RPORT in range(5000, 7001, 1):
        
        #socket object
        C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #connection timeout - just in case the server takes a second to respond
        C_SOCK.settimeout(2)
        
        try:

            #attempt a connection
            C_SOCK.connect((RHOST, RPORT))
            
            #if the connection is successful, send encoded data to server
            C_SOCK.send(SND_DATA.encode("utf8"))

            #if the right message is sent, some data will come back
            RCV_DATA = C_SOCK.recv(1024)

            #close the connection
            C_SOCK.close()

            #assign the decoded data and the port to a tuple to be used in printed output
            message_port = (RCV_DATA.decode("utf8"), RPORT)
            
            #break the loop
            break

        except socket.error:
            
            #if the connection is refused, close it, and the loop starts over
            C_SOCK.close()

    return message_port



#############
##ARGUMENTS##
#############

#create parser object
parser = argparse.ArgumentParser(description="")

#add --ipaddress argument
parser.add_argument("-i", "--ipaddress", dest="IP_ADDRESS", help="Enter an IP address", required=True)
parser.add_argument("-q", "--question", dest="Q_NUMBER", help="Enter an integer 1-5", required=True)

#parse the args
args = parser.parse_args()

#if no args were passed, print help
if len(sys.argv) == 1:
    print(parser.print_help())
    exit(0)



#############
##Main code##
#############

#create URL variable with formatted string
URL = f"http://{args.IP_ADDRESS}/q{args.Q_NUMBER}"

#print my full name
print("Gavin Hammer-Perdew\n")

#print the URL
print(URL, "\n")

#check what number was entered as -q/--question argument
#use it to determine what function to call or give error if invalid
#also use try/except to determine if address is valid, and give error if invalid

if args.Q_NUMBER == "1":
    try:
        answer = get_response(URL)
        print(f"Answer: {answer}\n")
    except:
        print(f"Invalid Address: {args.IP_ADDRESS}\n")

elif args.Q_NUMBER == "2":
    try:
        answer = parse_string(URL)
        print(f"Answer: {answer} Gavin\n")
    except:
        print(f"Invalid Address: {args.IP_ADDRESS}\n")

elif args.Q_NUMBER == "3":
    try:
        answer = parse_header(URL)
        print(f"Answer: {answer}\n")
    except:
        print(f"Invalid Address: {args.IP_ADDRESS}\n")

elif args.Q_NUMBER == "4":
    try:
        answer = parse_json(URL)
        print(f"Answer: {answer}\n")
    except:
        print(f"Invalid Address: {args.IP_ADDRESS}\n")

elif args.Q_NUMBER == "5":
    try:
        answer = socket_client(args.IP_ADDRESS)
        print(f"Answer: {answer[0]}\nPort: {answer[1]}\n")
    except:
        print(f"Invalid Address: {args.IP_ADDRESS}\n")

else:
    print(f"Invalid Question Number: {args.Q_NUMBER}\n")