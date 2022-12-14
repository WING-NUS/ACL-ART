'''
This script can be used to extract specific sections of the scholarly document from json files

Run script extract_data_from_json.py

Usage:

python extract_data_from_json.py -s <section_name> -i <input_path> -o <output_path>


<section_name> : Name of the section that is to be extracted. Possible section names: abstract, body, references

<input_path> : path to the input directory containing s2orc json files

<output_path> : output directory where the text file containing the extracted sections from all given json files will be stored

'''


import json
import os
import argparse


def extract_data_from_json(input_path, output_path, section):
    """
    Extract text from JSON file
    :param input_directory:
    :param output_file:
    :param section:
    :return:
    """
    
    with open(output_path, 'w') as fp:        
        for subdir, dirs, files in os.walk(input_path):
            for f in files:
                if f.endswith(".json"):
                    inputPath = os.path.join(subdir, f)
                    f = open(inputPath)
                    data = json.load(f)
                    content = extract_text(data, section)
                    for text in content:
                        fp.write("%s\n" % text)

def extract_text(data, section):
    content = []
    if section ==  "abstract":
        abstract = data["pdf_parse"]["abstract"]
        for ab in abstract:
            text = ab["text"]
            content.append(text)
    elif section == "references":
        references = data["pdf_parse"]["bib_entries"]
        for ref in references.items():
            raw_text = ref[1]["raw_text"]
            raw_text = raw_text.replace("- ","")
            content.append(raw_text)
    elif section == "body":
        abstract = data["pdf_parse"]["abstract"]
        for ab in abstract:
            text = ab["text"]
            content.append(text)
        bodyText = data["pdf_parse"]["body_text"]
        for txt in bodyText:
            text = txt["text"]
            content.append(text)
    return content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract data from json")
    parser.add_argument("-s", "--section", default=None, help="Section of json to extract")
    parser.add_argument("-i","--inputPath", default=None, help="Path to input json directory")
    parser.add_argument("-o","--outputPath",default=None, help="Path to output text file")

    args = parser.parse_args()

    input_path = args.inputPath
    output_path = args.outputPath
    section = args.section

    extract_data_from_json(input_path, output_path, section)