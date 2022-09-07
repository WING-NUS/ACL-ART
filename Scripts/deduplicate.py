import os
import argparse

def deduplicate(input_path):
    """
    Deletes older version of all files in a directory
    :param input_path:
    """
    for subdir, dirs, files in os.walk(input_path):
        for file1 in files:
            duplicates = []   
            if file1.endswith(".pdf"):   
                duplicates.append(file1) 
                for file2 in files:
                    if file2.endswith(".pdf"):
                        if file1.removesuffix('.pdf') + 'v' in file2.removesuffix('.pdf'):
                            duplicates.append(file2)
            if len(duplicates) > 1:
                latest = max(duplicates)
                duplicates.remove(latest)     
                for f in duplicates:
                    fname = os.path.join(subdir, f)     
                    print(f"Deleting File {fname}" )   
                    os.remove(fname)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deduplicate files in the given directory")
    parser.add_argument("-d", "--directory", default=None, help="Directory containing duplicate files")
  
    args = parser.parse_args()

    input_path = args.directory
   
    deduplicate(input_path)
 
    
   