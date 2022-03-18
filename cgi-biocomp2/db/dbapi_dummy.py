#!/usr/bin/python3
"""
...Comment header goes here...

This is the database API - it needs to access the MySQL database
"""

# Add the directory above to the module path to import the config file
import sys
sys.path.insert(0, "../")

import config  # Import configuration information (e.g. database connection)

def getAllEntries():
    """
    ...Function comment header goes here...

    This is a dummy function that returns a list of entries. The real version would probably
    return a list of dictionaries and would access the MySQL database
    """

    return(['AB000123', 'AB000321', 'AC001564'])

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

# Chromosomal Locations  (eg. 8q24.3)

def CDS_boundary_location():
    CDS_boundary_location=[1000,3000]
    return(CDS_boundary_location)

def Coding_regions():
    Coding_regions=[[1050,1070][2050,2030]]  


# CDS DNA String  (eg. gatcctccat)

def CDS_DNA_string():
    CDS_DNA_string='gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg'
    return(CDS_DNA_string)

# CDS amino acid string  (eg. MNRWVEKWLRVY)

def CDS_aa_string():
    CDS_aa_string='MNRWVEKWLRVYLKCYINLILFYRNVYPPQSFDYTTYQSFNLPQ'
    return(CDS_aa_string)

# whole genome DNA String  (eg. gatcctccat)


def whole_chromosome():
    whole_chromosome = 'gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg'
    return(whole_chromosome)

# list of codons (eg. [UUU,UUG,UUA])

def codons():
    codons=['UUU','UUG','UUA']
    return(codons)


# Restriction enzyme sequence dictionary (eg. [UUU,UUG,UUA])

def restriction_enz():
    restriction_enz={'EcoRI':'gattc', 'BamHI':'ggcct','BsuMI':'ccctta']
    return(restriction_enz)




