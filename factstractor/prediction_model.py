# -*- coding: utf-8 -*-
# TODO: attributes( facts, statements, definition )

"""
python -m spacy download en_core_web_lg
"""

import spacy
import csv
import pickle
import sys
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import argparse
import re
from tqdm import tqdm

def get_sentences( paragraphs ):
    _sentences = []
    for paragraph in paragraphs:
        paragraph = re.sub('.\[[0-9*]\]', '. ', paragraph)
        sentences = paragraph.split(". ")
        for sentence in sentences:
            sentence = sentence.replace("\n", "")
            # print(f">> sentence: {sentence}")
            if not sentence or sentence == "":
                continue
            _sentences.append( sentence )
    return _sentences

def read_file( filename ):
    readfile = open( filename, "r" )
    return readfile.readlines()

def load_fit_data( filename ):
    readfile = open( filename, 'rb')

    return pickle.load( readfile )

def write_to_csv_file(filename, data):
    with open(filename, mode='a+') as csvfile:
        csvfile_writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
        csvfile_writer.writerow( data )
        print("[+] File saved")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--from_file", "--ff", nargs=1, help='csv or pdf file')
    parser.add_argument("--predict", "--pp", nargs=1, help='predict from input text')
    args = parser.parse_args()

    readfromfile = False
    predict_only = False
    read_filename = ""
    
    if "from_file" in args:
        print(f">> reading from file: {args.from_file}")
        readfromfile = True
        read_filename = args.from_file[0]
    elif "ff" in args:
        print(f">> reading from file: {args.ff}")
        readfromfile = True
        read_filename = args.from_file[0]
    elif "predict" in args or "pp" in args:
        predict_only = True

    DATASET_FILENAME = "data_gathering/data/dataset.csv"
    nlp = spacy.load("en_core_web_lg")
    fit_filename = "trained_savefiles/trained_facts_classifier.obj"
    clf_svm_wv = load_fit_data( fit_filename )

    if readfromfile == True:
        # TODO: determine filetype, for now going with CSV
        text = read_file( read_filename )
        print(">> done readin document...")
        sentences = get_sentences( text )
        print(">> done splitting sentences...")

        for i in tqdm(range(len(sentences)), desc="fetching sentence..."):
            test_input = [ sentences[i] ]
            test_docs = [nlp(text) for text in test_input]
            test_input_vectors = [x.vector for x in test_docs]

            prediction = clf_svm_wv.predict( test_input_vectors )[0]
            if prediction == "facts":
                print(f"(prediction)$ ({test_input})_ |||||> {prediction}")
                input(">> press ENTER to continue...")
                print("")
        print(">> Done. Bye...")
