#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: Python Scripting Midterm Exam
"""

#print name
print("Name: Gavin Hammer-Perdew")


#open file slicing-file.txt
slicing_file = open("slicing-file.txt", "r", encoding="utf-8") #there is an apostrophe in eleventh_thirteenth that becomes gibberish without encoding


#store each word (line) separately in a list
slicing_list = slicing_file.readlines()


#############
##variables##
#############

#The third word from the end of the list
third_from_end = slicing_list[-3].replace("\n"," ")

#The third through fifth word of the list
third_thru_fifth = "".join(slicing_list[2:5:1]).replace("\n"," ")

#The 10th word from the end of the file and every other word for a total of 3 words
tenth_from_end = "".join(slicing_list[-10:-16:-2]).replace("\n"," ")

#The 11th through 13th word
eleventh_thirteenth = "".join(slicing_list[10:13:1]).replace("\n"," ")

#The 19th - 21st words from the end of the file
nineteenth_twentyfirst = " ".join(slicing_list[-19:-22:-1]).replace("\n","")


#########
##Quote##
#########

#add vars to new string var called "quote"
quote = third_from_end + third_thru_fifth + tenth_from_end + eleventh_thirteenth + nineteenth_twentyfirst

#print quote - output should be "Whether you think you can or you think you can't, you are right."
print(f'"{quote}"')
