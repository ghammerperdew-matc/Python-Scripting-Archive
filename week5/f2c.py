#! a/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: Defines a function for converting Fahrenheit to Celcius
"""

#function that converts F to C

def convert_temp(deg_fahr):

    deg_cel = (float(deg_fahr) - 32) * (5/9)

    return deg_cel


#main function for if the script is run directly

def main():
    print(convert_temp(32))


#if the script is run directly, main() is called

if __name__ == "__main__":
    main()
