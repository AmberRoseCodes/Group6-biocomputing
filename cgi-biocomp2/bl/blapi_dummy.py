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
    







#---------------------------------
# FRONT PAGE VARIABLES

# Identifier  (eg. BAA22866)

def id():
    id='BAA22866'
    return(id)

# Protein Product Name  (eg. glycosylphosphatidylinositol)

def ppn():
    ppn='glycosylphosphatidylinositol'
    return(ppn)

# Genbank Accession  (eg. ABB08360)

def genbank_acc():
    genbank_acc='ABB08360'
    return(genbank_acc)

# Chromosomal Accession  (eg. 8q24.3)

def chrom_acc():
    chrom_acc='8q24.3'
    return(chrom_acc)

#---------------------------------------
# DETAIL PAGE VARIABLES

# CDS Coding Region / Sticky end restriction enzymes / full origin sequence

def CDS_DNA_string():
    CDS_DNA_string='gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg'
    return(CDS_DNA_string)

def sticky_ends():
    sticky_end_EcoRI=[10, 20]
    sticky_end_BamHI=[5, 18]
    sticky_end_BsuMI=[8, 22]
    sticky_end_optional=[15, 25]
    return(sticky_EndEcoRI, sticky_end_BamHI, sticky_end_BsuMI, sticky_end_optional)

# CDS Amino Acid Seq

def CDS_aa_string():
    CDS_aa_string='MNRWVEKWLRVYLKCYINLILFYRNVYPPQSFDYTTYQSFNLPQ'
    return(CDS_aa_string)

# Entry Codon Useage Frequence / Whole chormosome Codon Useage Frequency

def codon_useage():
    A = [['UUU', 'UUG', 'UGA', 'TAG'], 
    [1.18, 0.8, 1.9, 0.5],
    [2, 0.8, 1.1, 1.9]]


