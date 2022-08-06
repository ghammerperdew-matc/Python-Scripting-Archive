#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: script for a chat server
"""



#imports

import socket



#variables

LHOST = ""

LPORT = 1234 #to match the client

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#bind to a port until script closes
L_SOCK.bind((LHOST, LPORT))


#print this to show it did something
print(f"Listening on port: {LPORT}")


while(True):

    L_SOCK.listen(1) #only need queue of 1 for this

    #accept the connection from client
    L_CONN, addr = L_SOCK.accept()

    #print to show successful connection
    print("Connected to ", addr)

    while(True):

        RCV_DATA = L_CONN.recv(1024)

        if not RCV_DATA or RCV_DATA.decode("utf8") == "exit":

            #breaking causes this script to close completely
            #"exit" is sent by the client, explanation is in client code
            break

        #show decoded data on server 
        print(f"The server received this data: {RCV_DATA.decode('utf8')}")

        #send the data back (still encoded)
        L_CONN.sendall(RCV_DATA)

    L_CONN.close()

exit()
