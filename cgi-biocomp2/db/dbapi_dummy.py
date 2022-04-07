#!/usr/bin/python3
"""
...Comment header goes here...

This is the database API - it needs to access the MySQL database
"""

# Add the directory above to the module path to import the config file
import sys
sys.path.insert(0, "../")

#import config  # Import configuration information (e.g. database connection)

def getAllEntries():
    """
    ...Function comment header goes here...

    This is a dummy function that returns a list of entries. The real version would probably
    return a list of dictionaries and would access the MySQL database
    """

    return([{'acc':'AB000321', 'gene_id':'gh56', 'ppn':'glucoselipid', 'chrom_loc':'103..600'},{'acc':'AB000322', 'gene_id':'gkk56', 'ppn':'glucoselipid-2', 'chrom_loc':'203..650'}])



# whole genome DNA String  (eg. gatcctccat)


def whole_chromosome():
    whole_chromosome = 'gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg'
    return(whole_chromosome)

# list of codons (eg. [UUU,UUG,UUA])

def codons():
    codons=['UUU','UUG','UUA']
    return(codons)


# Restriction enzyme sequence dictionary (eg. [UUU,UUG,UUA])

#def restriction_enz():
#    restriction_enz=['EcoRI':'gattc', 'BamHI':'ggcct','BsuMI':'ccctta']
#    return(restriction_enz)




