#!/usr/bin/env python3

#Author: Gavin Hammer-Perdew
#Description: This script prints several lines of formatted strings and numbers.


varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

#Prints Hello Timmy
print(f"Hello {varName}")

#Prints Red-Green-Blue
print(f"{varRed}-{varGreen}-{varBlue}")

#Prints Is this green or blue?
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")

#Prints My name is TIMMY
print(f"My name is {varName.upper()}")

#Prints [++Red++]
print(f"[{varRed:+^7s}]")

#Prints [green==]
print(f"[{varGreen.lower():=<7s}]")

#Prints [*****blue]
print(f"[{varBlue.lower():*>9s}]")

#Prints BlueBlueBlueBlueBlueBlueBlueBlueBlueBlue
print(f"{varBlue*10}")

#Prints 10.4516295
print(f"{varLoot}")

#Prints 10.5
#print(round(varLoot, 1)) ##I changed this to the code below
print(f"{varLoot:<.1f}")

#Prints I have $10.45
#print("I have $" + str(round(varLoot, 2))) ##I changed this to the code below
print(f"I have ${varLoot:<.2f}")

#Prints [$$$Red$$$] [$$$Green$$$] [$$$Blue$$$]
print(f"[{varRed:$^9s}] [{varGreen:$^11s}] [{varBlue:$^10s}]")

#Prints [ deR ][ Green ][ eulB ]
print(f"[{varRed[2::-1]: ^5s}][{varGreen: ^7s}][{varBlue[3::-1]: ^6s}]")

#Prints First Color:[Red] Second Color:[Green] Third Color:[Blue]
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
