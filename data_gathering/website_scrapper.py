#!/bin/python

import requests
import csv
from bs4 import BeautifulSoup
from tqdm import tqdm

# print( soup.prettify() )

foundCounter = 0

data_file = open('data/1000_facts.csv', 'w')
csvfile_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvfile_writer.writerow(['text', 'type'])
data_file.close()

def write_to_csv_file(data):
    with open('data/1000_facts.csv', mode='a+') as csvfile:
        csvfile_writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
        csvfile_writer.writerow([data, 'facts'])


def extract_attr(attr):
    global foundCounter

    props_attrs = soup.find_all(attr)
    for i in range(len(props_attrs)):
        pAttrs = props_attrs[i].get("class")
        if pAttrs is not None and "list" in pAttrs:
            foundCounter += 1
            # print( f"{foundCounter}: p|{props_attrs[i].get_text()}")
            write_to_csv_file(props_attrs[i].get_text().replace("\t", ""))


website = requests.get(f"https://www.thefactsite.com/1000-interesting-facts/")
website_text = website.text

soup = BeautifulSoup(website_text, 'html.parser')
for tag in ["p", "h2"]:
    extract_attr(tag)

for i in tqdm(range(1, 11), desc="Iterating through pages...."):
    website = requests.get(
        f"https://www.thefactsite.com/1000-interesting-facts/{i}/")
    website_text = website.text

    soup = BeautifulSoup(website_text, 'html.parser')
    list_attr = ["p", "h2"] 
    for attr in list_attr:
        extract_attr( attr )
