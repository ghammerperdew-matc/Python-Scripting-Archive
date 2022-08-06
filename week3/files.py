#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: reads from /etc/passwd multiple ways
"""


#open /etc/passwd as read only
passwd = open("/etc/passwd", "r")

#read the file and store full contents in a string variable --- read()
fileText = passwd.read()

#use len() to print the number of characters in the file
print("Length of the file: " + str(len(fileText))) #confirmed to be the same number as 'wc -c /etc/passwd'

#what does len() count and when would read() be used over other read functions?
print(
"""

In this case, 'len()' counts the number of characters stored in the variable.
The whole file happens to be stored as a string in this one variable.

The 'read()' function is generally used when completing operations on a whole file at once.
It is generally only used on smaller files, due to the need to place the whole file into memory
when it is assigned to a variable as seen in this technique.



""")




#open /etc/passwd as read only
passwd = open("/etc/passwd", "r")

#read the file and store full contents in a list variable --- readlines()
listText = passwd.readlines()

#use len() to print the number of items in the list
print("Length of the list: " + str(len(listText))) #confirmed to be the same number as 'wc -l /etc/passwd'

#what does len() count and when would readlines() be used over other read functions?
print(
"""

In this case, 'len()' counts the number of items in a list variable.
Each line is a separate item in the list, so 'len()' actually counts the number of lines.

The 'readlines()' function is generally used in situations when having each line stored separately
would be beneficial. An example would be a working with a list of usernames or emails.



""")




#open /etc/passwd as read only
passwd = open("/etc/passwd", "r")

#read the file one line at a time using a loop --- readline()
lineVar = passwd.readline() #gives the while loop a starting line
fileLength = 0 #total file length (number of characters)

while lineVar:   ##evaluates to true as long as it has a value
    fileLength += len(lineVar) #calcs the number of chars in the line and adds to total file length variable
    lineVar = passwd.readline() ##reads the next line -- when empty, the loop terminates

print(f"Length of the file: {fileLength}") #confirmed to be the same number as 'wc -c /etc/passwd'


#when would this technique be used over another read function?
print(
"""

The 'readline()' function is generally used when only part of a file needs to be processed/used
for a specific operation.



""")
