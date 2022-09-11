''' 
This utility is used to compute the hash values of the pdf files in the pdf folder.

Usage:

python computeHashes.py -f <file_list_path> -c <csv_path>

<file_list_path> : Path to the fileList.txt file containing the list of pdf files in the pdf folder

<csv_path> : Path to csv file where the file names with corresponding hash values will be stored


'''




import anthology.utils as anthology_utils
import os
import csv
import argparse
import time


def computeHashes(fileListPath, csvPath):
    with open(fileListPath,"r") as fp:
       files = fp.readlines()
    with open(csvPath, 'w') as f:
        writer = csv.writer(f)
        for f in files:
            fi = f.strip('\n')
            hashValue = anthology_utils.compute_hash_from_file(fi)
            row = [fi, hashValue]
            writer.writerow(row)
 
    numFiles = len(files)
    print(f"Computed hashes for {numFiles} files")

  
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compute hashes for pdf files")
    parser.add_argument("-f", "--fileListPath", default=None, help="path to the file containing list of files in pdf folder")
    parser.add_argument("-c", "--csvPath", default=None, help="path to csv file for storing hash values")

    args = parser.parse_args()

    fileListPath = args.fileListPath
    csvPath = args.csvPath

    startTime = time.time()

    computeHashes(fileListPath, csvPath)

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"The time taken is {elapsedTime} seconds")