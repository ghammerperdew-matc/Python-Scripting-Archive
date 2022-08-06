#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: Script usage output using argparse, also print values of entered arguments
"""


#imports

import argparse
import sys



#create parser object

parser = argparse.ArgumentParser(description="This is Gavin Hammer-Perdew's script")



#add arguments -- flags, decriptions (dest), metavar, help, etc.

#basic (text)
#note that this is the only one with a "dest" variable based on the image in the lab
parser.add_argument("-m", dest="basic", help="Enter some text")

#integer -- required??
parser.add_argument("-i", metavar="[an integer]", required=True, help="<required> Enter a simple integer")

#float
parser.add_argument("-d", metavar="[a float]", help="Enter a simple float")

#string - simple, single
parser.add_argument("-s", metavar="[a string]", help="Enter a simple string")

#multiple strings (list, space delimited)
parser.add_argument("-l", metavar="[strings] [[strings] ...]", nargs="*", help="Enter a list of strings (space delimited)")

#set default to true - needs an action and default
parser.add_argument("-t", "--set-true", default=False, action="store_true", help="Toggle from default False to True")

#set default to false - needs an action and default
parser.add_argument("-f", "--setfalse", default=True, action="store_false", help="Toggle from default True to False")

#version - needs an action
parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")



#parse the args

args = parser.parse_args()



#if no args were passed, print help

if len(sys.argv) == 1:
    
    print(parser.print_help())

    exit(0)



#Print the value of integer, string, float, list

print("The integer value entered is: ", args.i)

print("The string value entered is: ", args.s)

print("The float value entered is: ", args.d)

print("The list of strings is: ", args.l)
