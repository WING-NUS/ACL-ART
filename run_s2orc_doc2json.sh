#!/usr/bin/env bash
export ACL_ART_PROJECT_HOME=$HOME/Projects/ACL-ART

# put in your pdf2json directory here
python Scripts/run_s2orc_doc2json.py -i $ACL_ART_PROJECT_HOME/PDF -o $ACL_ART_PROJECT_HOME/Output_JSON -s $HOME/Projects/s2orc-doc2json

