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

def getAllEntries():
    """
    ...Function comment header goes here...

    This is a very simple function that just calls the database API to do the SQL to 
    obtain the full list of entries. It doesn't need to do anything else.
    """
    all_entries=dbapi_dummy.getAllEntries()
    return(all_entries)


#---------------------------------
# FRONT PAGE VARIABLES

# Identifier  (eg. BAA22866)

def gene_id():
    id='BAA22866'
    return(id)

# Protein Product Name  (eg. glycosylphosphatidylinositol)

def ppn():
    ppn='test'
    return(ppn)

# Genbank Accession  (eg. ABB08360)

def genbank_acc():
    genbank_acc='ABB08360'
    return(genbank_acc)

# Chromosomal Accession  (eg. 8q24.3)

def chrom_loc():
    chrom_loc='8q24.3'
    return(chrom_loc)

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


