#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: Python Scripting Midterm Exam
"""

#print my (author's) name to the screen
print("Name: Gavin Hammer-Perdew")

#counter variable -- adds line numbers of lines that contain keywords
Total = 0

#open file as read only
dataFile = open("Midterm-if.txt", "r")

#variable to store all lines except the header line as items in a list
listVar = dataFile.readlines()[1::]

#variable to count lines to use as list index number in loop
lineNumber = 0

#use loop to iterate through all items (lines) in the list
for line in listVar:
    
    #split line (list item) -- drop the new line character and separate by commas
    lineList = listVar[lineNumber].strip("\n").split(",")

    #check the list for each keyword, and add the line number to Total if list has keyword
    if "gmeach18@ed.gov" in lineList:
        Total += int(lineList[0])
    elif "248.253.63.149" in lineList:
        Total += int(lineList[0])
    elif "Whiteland" in lineList:
        Total += int(lineList[0])
    elif "80.222.19.190" in lineList:
        Total += int(lineList[0])
    elif "Kayley" in lineList:
        Total += int(lineList[0])
    elif "dcassyqw@microsoft.com" in lineList:
        Total += int(lineList[0])
    else:
        Total = Total
    
    lineNumber += 1

"""
The new line characters were making it so that the IPs (at the end of the lines) couldn't be searched for,
and instead of just changing the strings to have "\n" at the end, I just stripped it from every line.
So now if the order of the items in each line gets changed or a different file is used, it would still work.
At least I think it would still work.
"""

#print Total - should be 2425
print(f"The total is: {Total}")