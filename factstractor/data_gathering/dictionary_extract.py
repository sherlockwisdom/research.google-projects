#!/bin/python

import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import csv

url = 'https://www.thefreedictionary.com/'

nouns = open("data/nouns.txt", "r")

def write_to_csv_file(filename, data):
    with open(filename, mode='a+') as csvfile:
        csvfile_writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
        csvfile_writer.writerow(data)

def extract_attr(soup):
    global foundCounter

    props_attrs = soup.find_all("div")
    for attrs in props_attrs:
        _class = attrs.get("class")
        if _class and "ds-list" in _class:
            text = attrs.get_text()
            if "→" in text:
                continue
            text = re.sub('[0-9*]\.[\s*]', '', text )
            # print(f">>{text}")
            write_to_csv_file( filename="data/dataset.csv", data=[text, "definition"] )

        '''
        text = props_attrs[i].get_text().replace("\t", "")
        if not text.replace("\n", ""):
            continue

        text = text.replace("\n", ". ")
        if text:
            write_to_csv_file(text.replace("\t", ""))
            # print(f"{foundCounter}$_ {text}")
            foundCounter += 1
        '''

nouns = nouns.readlines()
for i in tqdm(range(len(nouns)), desc="processing nouns..."):
    noun = nouns[i].replace('\n', '')
    turl = url + noun
    # print( turl)

    request = requests.get(turl)
    soup = BeautifulSoup(request.text, 'html.parser')
    extract_attr(soup)
    # input("")

