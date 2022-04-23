#!/usr/bin/python3
"""
...Comment header goes here...

This is the business logic API
"""

# Add the bl sub-directory to the module path (for testing this routine)
# and the directory above to import the config file
import sys
sys.path.insert(0, "../db/")
sys.path.insert(0, "../")

import dbapi_dummy   # Import the database api
#import config  # Import configuration information (if needed)
import re

def getAllEntries():
    """
    ...Function comment header goes here...

    This is a very simple function that just calls the database API to do the SQL to 
    obtain the full list of entries. It doesn't need to do anything else.
    """
    all_entries=dbapi_dummy.getAllEntries()
    return(all_entries)


#---------------------------------

def getAnEntry(ac):
    for d in getAllEntries():
        if d['acc']==ac:
            return(d)

# Identifier  (eg. BAA22866)

def gene_id(ac):
    gene_id=getAnEntry(ac)['gene_id']
    return(gene_id)

# Protein Product Name  (eg. glycosylphosphatidylinositol)

def ppn(ac):
    ppn=getAnEntry(ac)['ppn']
    return(ppn)


# Chromosomal Accession  (eg. 8q24.3)

def chrom_loc(ac):
    chrom_loc=getAnEntry(ac)['chrom_loc']
    return(chrom_loc)

# CDS Coding Region 

def CDS_DNA_string(ac):
    CDS_DNA_string=getAnEntry(ac)['CDS_DNA_string']
    return(CDS_DNA_string)

# CDS Amino Acid Seq

def CDS_aa_string(ac):
    CDS_aa_string=getAnEntry(ac)['CDS_aa_string']
    return(CDS_aa_string)


# Translate function


def translate(DNA):
  n_trans_dict = {'a': 'u', 't':'a', 'c': 'g', 'g': 'c'}
  transtable = DNA.maketrans(n_trans_dict)
  rna = DNA.translate(transtable)
  return(rna)

def codon_count(ac):
    counts=[]
    rna = translate(CDS_DNA_string(ac).lower())
    rna_codon = [rna[i:i+3] for i in range(0,len(rna), 3)]
    for i in dbapi_dummy.codons():
        count = rna_codon.count(i)
        string = i + ' : ' + str(count) + '   '
        counts.append(string)
    return(counts)


def sticky_ends_loc(ac,enzyme):
    matches=[]
    recognition_site=sticky_ends()[enzyme][0]
    for m in re.finditer(recognition_site, CDS_DNA_string(ac)):
        matches.append(m.start()+sticky_ends()[enzyme][1])
    return(matches)  
    






