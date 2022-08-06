#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: script for a file transfer server
"""

#imports
import socket



#open file or create it if it doesn't exist
writeFile = open("testFile2.txt", "w")


#assign address/port to variables
#LHOST will be empty string to listen on all available interfaces
LHOST = ""

LPORT = 1234


#make variable for data to be received
RCV_DATA = ""


#create socket object
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#bind to interface/port
L_SOCK.bind((LHOST, LPORT))


#listen for connection
L_SOCK.listen(1)

print(f"Listening on port: {LPORT}")


#accept connection
L_CONN, addr = L_SOCK.accept()

print("Connected to ", addr)

#receive and decode data
RCV_DATA = L_CONN.recv(1024)


#write decoded (utf8) data to open file and close it
writeFile.write(RCV_DATA.decode("utf8"))


#if file doesn't get closed, it doesn't save
writeFile.close()

#close connection
L_CONN.close()
