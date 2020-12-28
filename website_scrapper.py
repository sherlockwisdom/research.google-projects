#!/bin/python

import requests
from bs4 import BeautifulSoup

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


website = requests.get(f"https://www.thefactsite.com/1000-interesting-facts/")
website_text = website.text

soup = BeautifulSoup( website_text, 'html.parser' )
for tag in ["p", "h2"]:
	extract_attr( tag )

for i in range( 1, 11 ):
	website = requests.get(f"https://www.thefactsite.com/1000-interesting-facts/{i}/")
	website_text = website.text

	soup = BeautifulSoup( website_text, 'html.parser' )
	for tag in ["p", "h2"]:
		extract_attr( tag )
