'''
This script can be used to run s2orc-doc2json toolkit on a set of pdf files in a folder to obtain s2orc json files

Usage: 

python run_s2orc_doc2json.py -i <input_path> -o <output_path> -s <s2orc_path>

<input_path> : path to the input directory containing PDF files

<output_path> : path to the output dir for putting json files

<s2orc_path>  : path to root directory of s2orc-doc2json toolki

'''

import os
import time
import argparse

def run_s2orc_doc2json(inputFolder, outputFolder, s2orcFolderPath):
    for subdir, dirs, files in os.walk(inputFolder):
        for f in files:
            if f.endswith(".pdf"):
                inputPath = os.path.join(subdir, f)
                outputSubdir = subdir.partition('pdf')[2]
                prefix_letter = outputSubdir[1].upper()
                outputPath = outputFolder + f"/prefix{prefix_letter}/json/"+ outputSubdir
                s2orcPath = s2orcFolderPath + '/doc2json/grobid2json/process_pdf.py'
                command = "python " + s2orcPath + " -i" + inputPath + " -t temp/ -o " + outputPath
                print(f"Start processing {f}!")
                os.system(command)
                print(f"{f} file has been converted!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run s2orc-doc2json tool")
    parser.add_argument("-i", "--inputPath", default=None, help="path to the input directory containing PDF files")
    parser.add_argument("-o", "--outputPath", default=None, help="path to the output dir for putting json files")
    parser.add_argument("-s", "--s2orcFolderPath", default=None, help="path to root directory of s2orc-doc2json toolkit")

    args = parser.parse_args()

    inputPath = args.inputPath
    outputPath = args.outputPath
    s2orcFolderPath = args.s2orcFolderPath

    startTime = time.time()

    run_s2orc_doc2json(inputPath, outputPath, s2orcFolderPath)

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"The overall time taken to process all files is {elapsedTime} seconds")
