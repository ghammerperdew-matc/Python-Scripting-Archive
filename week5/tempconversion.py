#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew

Description:
Uses the convert_temp function from f2c.py to convert a temperature
input by a user from fahrenheit to celcius and prints it to the screen
"""

#imported modules

import f2c


#get user input for a temperature (degrees fahrenheit)

temp_fahr = input("Please enter a temperature in degrees Fahrenheit: ")


#call convert_temp() from f2c to convert the input temp to degrees celcius

temp_cel = f2c.convert_temp(temp_fahr)


#print temp_cel rounded to two decimal points

print(f"{temp_fahr} degrees Fahrenheit converted to degrees Celcius is {temp_cel:<.2f}")

