#!/bin/python

import requests
import csv
from bs4 import BeautifulSoup
from tqdm import tqdm

# print( soup.prettify() )

foundCounter = 0

DATA_FILENAME = "data/dataset.csv"

def write_to_csv_file(data):
    with open(DATA_FILENAME, mode='a+') as csvfile:
        csvfile_writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
        csvfile_writer.writerow([data, 'statements'])

def extract_attr(soup, attr):
    global foundCounter

    props_attrs = soup.find_all(attr)
    for i in tqdm(range(len(props_attrs)), "Extracting data..."):
        if props_attrs[i].get("class"):
            continue

        text = props_attrs[i].get_text().replace("\t", "")
        if not text.replace("\n", ""):
            continue

        text = text.replace("\n", ". ")
        if text:
            write_to_csv_file(text.replace("\t", ""))
            # print(f"{foundCounter}$_ {text}")
            foundCounter += 1

website = requests.get(f"https://englishgrammarhere.com/speaking/100-english-sentences-used-in-daily-life/")
website_text = website.text

soup = BeautifulSoup(website_text, 'html.parser')
for tag in ["li"]:
    extract_attr(soup, tag)
