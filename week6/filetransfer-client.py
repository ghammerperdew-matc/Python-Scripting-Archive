#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: script for a file transfer client
"""

#imports
import socket



#assign address/port info to variables

hostName = socket.gethostname()

RHOST = socket.gethostbyname(hostName)

RPORT = 1234


#create socket variable/object
C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#open file (read only in this case)
readFile = open("testFile1.txt", "r")


#read file into variable (whole file all at once)
fileData = readFile.read()


#connect socket to address/port previously identified
C_SOCK.connect((RHOST, RPORT))


#encode data (utf8) and send
C_SOCK.send(fileData.encode("utf8"))


#close the connection
C_SOCK.close()
