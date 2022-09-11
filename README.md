# ACL-ART

## Description

The ACL Anthology Rich Text corpus (ACL-ART) is a scholarly corpus in computational linguistic domain, obtained and processed from [ACL Anthology](https://aclanthology.org/). The documents are made available in pdf and s2orc json formats. Annotated datasets for downstream NLP tasks such as Citation Intent Classification are also provided. It provides full text of all documents in the ACL Anthology Collection( 74,313 files) until July 2022 in PDF and json formats.

This corpus is under active development at National University of Singapore (NUS), Singapore. 

## ACL ART Structure

pdf/ - PDFs of all files in the ACL Anthology website 

json/ - s2orc json files of all the PDFs in the pdf/ folder 

docs/ - contains the list of files in the pdf directory, hashes of PDFs

annotated_datasets/ - contains annotated datasets for various downstream NLP tasks

## Steps to reproduce this corpus

1) Download pdf files from ACL Anthology web server

We use the ``` make mirror ``` command as specified in the [ACL Anthology repository](https://github.com/acl-org/acl-anthology). The files will be available in the build folder. 

To compute hash values of the pdf files, run the utility computeHashes.py from Docs folder. We use a custom function provided by anthology.utils to compute hashes. Refer [here](https://aclanthology.org/info/development/) for setup. Ensure that Docs folder is in the same directory as pdf folder.


2) Convert pdf files to machine readable format

We use, s2orc-doc2json tooklit for this. To set up s2orc-doc2json toolkit, follow the instructions provided in the [s2orc-doc2json repository](https://github.com/allenai/s2orc-doc2json). After setting up and running s2orc-doc2json toolkit, run the script run_s2orc_doc2json.py from Scripts folder.
  
