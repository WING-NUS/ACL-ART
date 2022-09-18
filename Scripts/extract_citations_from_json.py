'''
This script can be used to extract citations from s2orc json files

Run script extract_citations_from_json.py

Usage:

python extract_citations_from_json.py -i <input_path> -o <output_path>

<input_path> : Path to folder containing s2orc json files

<output_path> : Path to csv file to store citations

'''

import os
import json
from spacy.matcher import PhraseMatcher
import spacy
import re

import argparse
import csv
import time
from nltk.tokenize import sent_tokenize

def extract_citations(input_path, output_path): 
    with open(output_path,'w') as csvfile:
        csvwriter = csv.writer(csvfile) 
        for subdir, dirs, files in os.walk(input_folder):
            for f in files:
                if f.endswith(".json"):
                    citations = []
                    input_path = os.path.join(subdir, f)
                    f = open(input_path)
                    data = json.load(f)
                    body_text = data["pdf_parse"]["body_text"]
                    citations += match_pattern(body_text)
                    for citation in citations:
                      csvwriter.writerow([citation])     


def match_pattern(body_text):
    citations = []
    for t in body_text:
        text = t['text']
        citation = t['cite_spans']
        phrases = []
        for c in citation:
            b = c['ref_id']
            if b != None:
            phrases.append(c['text'])
        sentences = sent_tokenize(text)       
        for line in sentences:
            for cite in phrases:
                if cite in line and line not in citations:
                    citations.append(line)        
    return citations


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract sentences containing citations from s2orc json files")
    parser.add_argument("-o", "--outputPath", default=None, help="csv file path to store citations")
    parser.add_argument("-i", "--inputPath", default=None, help="Directory containing json files")

    args = parser.parse_args()
    input_path = args.inputPath
    output_path = args.outputPath


    startTime = time.time()
    extract_citations(input_path, output_path)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"The time taken is {elapsedTime} seconds")