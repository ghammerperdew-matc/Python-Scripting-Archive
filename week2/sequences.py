#!/usr/bin/env Python3

"""
Author: Gavin Hammer-Perdew
Description: This script prints sliced strings/lists.
"""

varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]


"""
varString section
"""
#Prints e is a nice string to slice
print(varString[3::1])

#Prints Her
print(varString[0:2:1])

#Prints e is a ni
print(varString[3:11:1])

#Prints Hr sanc tigt lc
print(varString[::2])

#Prints ecils ot gnirts ecin a si ereH
print(varString[::-1])


"""
varList section
"""
#Prints ['slice','to','list','nice','a','is','Here']
print(varList[::-1])

#Prints ['a','is','Here']
print(varList[2::-1])

#Prints ['a','nice']
print(varList[2:4])

#Prints ['Here','nice','slice']
print(varList[0::3])

#Prints ['is','a','nice','list','to','slice']
print(varList[1::])


"""
loops to iterate through the variables one element at a time

note: I frequently use i or x in loops because it is shorter/easier, and it's how I first learned
"""

for i in varString:
    print(i)

for i in varList:
    print(i)
