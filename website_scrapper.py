#!/bin/python

import requests
from bs4 import BeautifulSoup

website = requests.get("https://www.thefactsite.com/1000-interesting-facts/")
website_text = website.text

soup = BeautifulSoup( website_text, 'html.parser' )
# print( soup.prettify() )

foundCounter = 0
ps = soup.find_all('p')
for i in range(len(ps)):
	pAttrs = ps[i].get("class")
	if pAttrs is not None and "list" in pAttrs:
		foundCounter += 1
		print( f"{foundCounter}: {ps[i].get_text()}")
