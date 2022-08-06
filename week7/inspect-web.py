#!/usr/bin/env python3

"""
Author: Gavin Hammer-Perdew
Description: gets a list of links from a webpage (notpurple.com in this case)
"""

#imports

import requests
import bs4 ###beautiful soup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/



#get the webpage

response = requests.get("https://notpurple.com")



#assign html text content to a bs4 object var

soupVar = bs4.BeautifulSoup(response.text, "html.parser")



#print title

print(soupVar.select("head > title"))



#print links

## I didn't know how many links it would return,
## and I don't like looking at list items, so I printed each item

for link in soupVar.select("a"):
    print(link)
