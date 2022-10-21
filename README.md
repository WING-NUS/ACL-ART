# ACL-ART

## Description

The ACL Anthology Rich Text corpus (ACL-ART) is a scholarly corpus in computational linguistic domain, obtained and processed from [ACL Anthology](https://aclanthology.org/). The documents are made available in pdf and s2orc json formats. Human annotated datasets for downstream NLP tasks such as Citation Intent Classification are also provided. It provides full text of all documents in the ACL Anthology Collection (74,313 files) until July 2022 in PDF and json formats.

This corpus is under active development at National University of Singapore (NUS), Singapore. 

## ACL ART Corpus

The ACL ART Corpus can be accessed [here](https://drive.google.com/drive/folders/1RQdsRROlz7JXG5UF2OQfcKbYkhix-9DL?usp=sharing). Note that, originial files in ```pdf``` and ```json``` directories are organized by venues, we compressed these files by the prefix of venues. For example prefixA.zip contains all files in venues ```A, aacl, acl, adaptnlp, aespen, ai4hi, alta``` and etc.

```
├──pdf/ - PDFs of all files in the ACL Anthology website 

├──json/ - s2orc json files of all the PDFs in the pdf/ folder 

├──docs/ - contains the list of files in the pdf directory, hashes of PDFs

├──annotated_datasets/ - contains annotated datasets for various downstream NLP tasks
```

## Steps to reproduce this corpus

### Download PDF files from ACL Anthology

The [ACL Anthology](https://aclanthology.org/) is frequently updated. They have a github repository [acl-anthology](https://github.com/acl-org/acl-anthology) for easy management. After ```git clone https://github.com/acl-org/acl-anthology```, we use the recommended ``` make mirror ``` command to download all PDF files, which runs ```./bin/create_mirror.py```. The PDF files can be founded ```./build/anthology-files/pdf/```, organized in venues.

We provide documentation files of the ACL ART corpus, including file lists, hashes of all files. To compute hash values of the pdf files, run the utility computeHashes.py from ```docs``` folder. We use a custom function provided by anthology.utils to compute hashes. Refer [here](https://aclanthology.org/info/development/) for setup. Ensure that Docs folder is in the same directory as pdf folder.


### Convert PDF files to machine readable format

In order to maintain same format with another scholarly corpus S2ORC from AllenAI, we adopt the json format for full text files. And we use [s2orc-doc2json](https://github.com/allenai/s2orc-doc2json) tooklit for extracting structured full text from PDF files. To set up s2orc-doc2json toolkit, follow the instructions provided in the [s2orc-doc2json repository](https://github.com/allenai/s2orc-doc2json). After setting up and running s2orc-doc2json toolkit, follow the steps below for full text extraction:

1. Create an input folder called ```PDF``` in your root directory 
2. Create an output folder called ```Output_JSON``` in your root directory
3. Make sure the paths match your directory path. Open the ```run_s2orc_doc2json.sh``` file and edit the first line to point to this project folder.
4. Run the necessary scripts by calling ```bash run_s2orc_doc2json.sh```


## Rich Information Extraction

We aim to extract rich information from the extracted full text files with state-of-the-art NLP toolkits. This is an On-going work.

### Citation Intent Classification

Citations play a crucial role in scientific discourse. We provide a machine annotated dataset for Citation Intent Classification. Citation Intent Classification aims to classify citation contexts based on their intent to make it easier for the users to understand why a specific author cited another paper. 

We used [Scibert](https://github.com/allenai/scibert), finetuned on the [Scicite dataset](https://allenai.org/data/scicite) for this. Based on their intent, citations are classified into 3 categories - background (providing background information), method (use of a method, tool or a dataset) and result (comparison of results).

We followed the instructions specified in the [Scibert repository](https://github.com/allenai/scibert) to fine tune the model and make predictions. We used ```scibert-scivocab-uncased``` as the base model, learning rate of ```2e-5``` for ```2 epochs``` as mentioned [here](https://arxiv.org/pdf/1903.10676.pdf) and we were able to reproduce similar results. We also validated the predictions on a human annotated test set contatining 95 citations. The model gave a macro averaged F score of 68. 

## Collaboration

We hope this corpus to be a collaborative corpus, just as a previous version [ACL ARC corpus](https://catalog.ldc.upenn.edu/docs/LDC2009T29/lrec_08/) did. We hope you can contribute effort to convert PDF files to JSON full text files as well as Rich Information Extraction part. If you are interested in this project, please drop us an email to [Dr. Yanxia Qin](qolina@gmail.com).
