#!/bin/python

import requests
from bs4 import BeautifulSoup

website = requests.get("https://www.thefactsite.com/1000-interesting-facts/")
website_text = website.text

soup = BeautifulSoup( website_text, 'html.parser' )
# print( soup.prettify() )

foundCounter = 0
def extract_attr( attr ):
	global foundCounter
	props_attrs = soup.find_all( attr )
	for i in range(len(props_attrs)):
		pAttrs = props_attrs[i].get("class")
		if pAttrs is not None and "list" in pAttrs:
			foundCounter += 1
			print( f"{foundCounter}: p|{props_attrs[i].get_text()}")

for tag in ["p", "h2"]:
	extract_attr( tag )
