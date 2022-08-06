#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew

Description: runs system command to get a list of running processes and format it into usable data
"""

#import the subprocess module
import subprocess


#run the command and store the output by passing it from the running
#subprocess (command that was just run) using PIPE

myProc = subprocess.run(["ps","-axco","command"], stdout = subprocess.PIPE)


#use decode() to extract the data from myProc.stdout (piped data from previously running subprocess)
#and store in myProcString

myProcString = myProc.stdout.decode()


#use split("\n") to create a list from myProcString and store in myProcList

myProcList = myProcString.split("\n")


#use a loop to print each item in myProcList one at a time

for process in myProcList:
    print(process)


#print the number of processes in the list using len() - skip the first line

print("The number of processes is " + str(len(myProcList[1::])))