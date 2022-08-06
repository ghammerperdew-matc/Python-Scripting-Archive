#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: script for a chat client
"""



#imports

import socket



#variables

#I got an error when trying to use gethostbyname("ident.me")
#Probably due to not having a name to actually give it in the first place
#If there is another reason, please tell me
hostName = socket.gethostname()

RHOST = socket.gethostbyname(hostName)

RPORT = 1234 #I checked that this wasn't open using netstat

SND_DATA = "" #empty for now to receive input later

RCV_DATA = "" #used to catch data sent from server

#make socket object/variable
C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#connect to specified
C_SOCK.connect((RHOST, RPORT))


while(True):

    USER_DATA = input("Enter some text: ")

    if USER_DATA.lower() == "exit":

        #make lowercase again, encode and send exit message
        C_SOCK.send(USER_DATA.lower().encode("utf8"))

        #break while loop
        break

        """
        The server script is designed to close completely as well on exit.
        That is why I send "exit" instead of just breaking.
        I did this for ease of use during testing.
        I wrote this on my windows machine so I can have 4 monitors,
        and cmd doesn't like to close my python script with ctrl + c for some reason.
        I wanted to be able to keep that cmd session open and still end the script.
        I realize I could run it with the python interpreter itself, but that's no fun.
        """

    else:

        #encode data (utf8 byte array) and send it
        C_SOCK.send(USER_DATA.encode("utf8"))

        #catch whatever is thrown back across the connection (should be same data)
        RCV_DATA = C_SOCK.recv(1024)

        #decode and print out whatever comes back (should be same as what was sent)
        print(RCV_DATA.decode("utf8"))

#close the connection when the loop breaks
C_SOCK.close()
