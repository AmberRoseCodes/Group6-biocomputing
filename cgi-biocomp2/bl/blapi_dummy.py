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

# CDS Amino Acid Seq

def CDS_aa_string(ac):
    CDS_aa_string=getAnEntry(ac)['CDS_aa_string']
    return(CDS_aa_string)

# joins

def joins(ac):
    joins=getAnEntry(ac)['joins']
    return(joins)

# complement

def complement(ac):
    copmlement=getAnEntry(ac)['complement']
    return(complement)

# Translate 

def translate(DNA):
  n_trans_dict = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}
  transtable = DNA.maketrans(n_trans_dict)
  rna = DNA.translate(transtable)
  return(rna)

# CDS Coding Region 

def CDS_DNA_string(ac):

# Returns the full origin CDS sequence from the genbank file, translating the string if it is flagged as being a complementary strand

    if complement(ac) == '1':
        CDS_DNA_string=translate(getAnEntry(ac)['CDS_DNA_string'])
    else: 
        CDS_DNA_string=getAnEntry(ac)['CDS_DNA_string']

    return(CDS_DNA_string)

# Create a  list of tuples with all exon locations (Input: Accession Number)

def exon_tuples(ac):
    join_string=joins(ac)
    start_r='\'([0-9]+)\.\.'
    end_r='\.\.([0-9]+)\''
    start=re.findall(start_r,join_string)
    end=re.findall(end_r,join_string)
    exon_tuples=[]
    x=0
    for i in start:
        exon=[]
        exon=tuple((int(i),int(end[x])))
        x+=1
        exon_tuples.append(exon)
    exon_tuples.sort
    return(exon_tuples)

# Create a string, with CDS origin length, noting the exon locations (Input: Accession Number)

def exon_string(ac):
    exons_joined=exon_tuples(ac)
    exon_string=[]
    for n in CDS_DNA_string(ac):
        exon_string.append('-')

    for n in range(0,len(exon_string),1):
        for a,b in exons_joined: 
            if n>=(a-1) and n<=b:
                exon_string[n]='*'

    return(exon_string)

# Leverages the exon location information to create the CDS DNA string

def exon_DNA_string(ac):
    exon_DNA_string=[]
    exons= exon_tuples(ac)
    x=0
    for n in CDS_DNA_string(ac):
        for a,b in exons: 
            if x>=(a-1) and x<=(b-1):
                exon_DNA_string.append(n)
        x+=1
    return(''.join(exon_DNA_string))



# Transcribe forward strand DNA to RNA (non-specific function)


def transcribe(DNA):
  n_trans_dict = {'T': 'U'}
  transtable = DNA.maketrans(n_trans_dict)
  rna = DNA.translate(transtable)
  return(rna)


# Count codon useage across the CDS DNA String

def codons():
    codons=['UUU','UUC','UUA','UUG','AUU','AUC','AUA','AUG','GUU','GUC','GUA','GUG','UCU','UCC','UCA','UCG','CUU','CUC','CUA','CUG','CCU','CCC','CCA',
'CCG','ACU','ACC','ACA','ACG','GCU','GCC','GCA','GCG','UAU','UAC','UAA','UAG','CAU','CAC','CAA','CAG','AAU','AAC','AAA','AAG','GAU','GAC','GAA','GAG',
'UGU','UGC','UGA','UGG','CGU','CGC','CGA','CGG','AGU','AGC','AGA','AGG','GGU','GGC','GGA','GGG'
]
    return(codons)

def codon_count(ac):
    counts=[]
    rna = transcribe(exon_DNA_string(ac))
    rna_codon = [rna[i:i+3] for i in range(0,len(rna), 3)]
    for i in codons():
        count = rna_codon.count(i)
        string = i + ' : ' + str(count) + '   '
        counts.append(string)
    return(counts)

 # Create a static dictionary continaed within a function to provide information about Restriction 

def sticky_ends():
    
# -------------------------------------------------------
# Dictionary contains the regognition site for each enzyme, and the index at which it leaves a sticky end on the  # enzyme, in each case the recognition site is noted from the 5 prime end
# -------------------------------------------------------

    sticky_ends={'EcoRI':['GAATTC',0], 'BamHI':['GGATCC',0], 'BsuMI':['ACCTGC',9]}

    return(sticky_ends)

 # Create a list with locations of the sticky ends (Inputs: Restriction Enzyme & Accession Number)

def sticky_ends_loc(ac,enzyme):
    matches=[]
    recognition_site=sticky_ends()[enzyme][0]
    for m in re.finditer(recognition_site, CDS_DNA_string(ac)):
        matches.append(m.start()+sticky_ends()[enzyme][1])
    return(matches)  

 # Create a string, with CDS origin length, noting the restriction enzyme locations (Input: Accession Number)

def sticky_ends_inplace(ac): 
    l=[]
    for n in CDS_DNA_string(ac):
        l.append('-')
    for i in sticky_ends():
        se=sticky_ends_loc(ac,i)
        x=0
        for n in l:
            if x in se :
                l[x]=i
            elif l[x]=='-':
                l[x]='-'
            x+=1
    return(l)




