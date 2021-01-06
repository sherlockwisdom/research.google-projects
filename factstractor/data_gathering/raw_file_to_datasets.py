#!/bin/python

import csv

DATA_FILENAME = "data/dataset.csv"
def write_to_csv_file(data):
    with open(DATA_FILENAME, mode='a+') as csvfile:
        csvfile_writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
        csvfile_writer.writerow([data, 'facts'])



rawfile = "data/raw_sentences.txt"

csvfile = open( rawfile, "r")
Lines = csvfile.readlines()


for line in Lines:
    if line:
        write_to_csv_file( line )
