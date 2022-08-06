#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: copies a website (notpurple.com in this case) to an html file
"""

#imports

import requests



#get the website

response = requests.get("https://notpurple.com")



#open a file to which to write said website

writeFile = open("my_web_file.html", "w")



#write the html content from website to the file

writeFile.write(response.text)



#close the file so that it can save

writeFile.close()
