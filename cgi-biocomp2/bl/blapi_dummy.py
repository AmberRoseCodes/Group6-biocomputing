#!/usr/bin/python3

"""

This is the business logic API

Author: Amber Hilton

Current version: V10

Version History: 

--------------------------------------
V1  | Established the Dummy API code
V2  | Updated the Dummy API code following design itteration
V3  | Created Variable functions to return entity specific variables
V4  | Created Sticky End Fucntions
V5  | Created entity codon count Functions
V6  | Created String functions to align Sticky Ends and Exons to the full origin sequence
V7  | Created translate and transcribe functions and function to stich exon DNA regions together
V8  | Updated functions to point at Exon DNA region rather than Full origin sequence where required
V9  | Updated codon count Functions to include full chromosome % and entity specific % 
V10 | Updated API file with documentation [ Current working Version ]
--------------------------------------

"""

# Add the bl sub-directory to the module path (for testing this routine)
# and the directory above to import the config file

import sys
sys.path.insert(0, "../db/")
sys.path.insert(0, "../")

import dbapi   # Import the database api
import re # Import Regex library


#---------------------------------

# GLOBAL FUNCTIONS

def getAllEntries():
    """
    GET ALL ENTRIES

This function calls the database API which connects directly to the MariaDB which contains all the raw data extracted from genbank. The function returns the data in the form of a list of dictionaries, each dictionary returning each attribute required for each genbank entry. 

    """
    all_entries=dbapi.getAllEntries()
    return(all_entries)


#---------------------------------

# ENTITIY SPECIFIC ATTRIBUTE EXTRACTION FUNCTIONS

def getAnEntry(ac):

    """
    GET AN ENTRY

This function returns a dictionary of attributes for a specific Genbank entry, specified by the Accession Number. 

    """

    for d in getAllEntries():
        if d['acc']==ac:
            return(d)


def gene_id(ac):

    """
    GET GENE ID

This function returns the gene id from the dictionary of attributes for a specific Genbank entry, specified by the Accession Number. 

    """
    gene_id=getAnEntry(ac)['gene_id']
    return(gene_id)


def ppn(ac):

    """
    GET PROTEIN PRODUCT NAME

This function returns the protein product name from the dictionary of attributes for a specific Genbank entry, specified by the Accession Number. 

    """
    ppn=getAnEntry(ac)['ppn']
    return(ppn)



def chrom_loc(ac):

    """
    GET CHROMOSOMAL LOCATION (eg. 8q24.3)

This function returns the chromosomal location code from the dictionary of attributes for a specific Genbank entry, specified by the Accession Number. 

    """
    chrom_loc=getAnEntry(ac)['chrom_loc']
    return(chrom_loc)


def CDS_aa_string(ac):

    """
    GET CDS AMINO ACID CODE

This function returns the amino acid string from the dictionary of attributes for a specific Genbank entry, specified by the Accession Number. 

    """
    CDS_aa_string=getAnEntry(ac)['CDS_aa_string']
    return(CDS_aa_string)


def joins(ac):

    """
    GET EXON LOCATIONS

This function returns the exon locations from the from the dictionary of attributes for a specific Genbank entry, specified by the Accession Number. 

    """
    joins=getAnEntry(ac)['joins']
    return(joins)


def complement(ac):

    """
    GET COMPLEMENT STATUS

This function returns the complement status from the from the dictionary of attributes for a specific Genbank entry, specified by the Accession Number. (Indicating if the DNA string listed in the genbank entry is the complimentary strand, a value of 1 means the entry is complementary)

    """
    copmlement=getAnEntry(ac)['complement']
    return(complement)

def CDS_DNA_string(ac):

    """
    GET CDS DNA STRING (ORIGIN)

This function returns the CDS origin DNA string from the dictionary of attributes for a specific Genbank entry, specified by the Accession Number. (If the complementary attribute is set to 1, the DNA string is translated to reflect the forward strand)

    """

    if complement(ac) == '1':
        CDS_DNA_string=translate(getAnEntry(ac)['CDS_DNA_string'])
    else: 
        CDS_DNA_string=getAnEntry(ac)['CDS_DNA_string']

    return(CDS_DNA_string)

#---------------------------------

# ENTITIY SPECIFIC ATTRIBUTE TRANSFORMATION FUNCTIONS



def translate(DNA):

#DNA TRANSLATION

#This function translates DNA in the form of a string from one strand to the other, mostly useful for the complementary strand transformation and not likley to be called by the front end.

  n_trans_dict = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}
  transtable = DNA.maketrans(n_trans_dict)
  rna = DNA.translate(transtable)
  return(rna)



def exon_tuples(ac):

#EXON LOCATION 

#This function transforms the join attribute into a list of tuples, mostly useful for identifying the location of the coding regions (exons) and not likley to be called by the front end.


    join_string=joins(ac)
    start_r='\'([0-9]+)\.\.'
    end_r='\.\.([0-9]+)\''
    start=re.findall(start_r,join_string)
    end=re.findall(end_r,join_string)
    exon_tuples=[]
    x=0
    for i in start:
        
        try:
            exon=tuple((int(i),int(end[x])))
        except:
            pass
        exon_tuples.append(exon)
        x+=1
    exon_tuples.sort
    return(exon_tuples)



def exon_string(ac):

# Create a string, with CDS origin length, noting the exon locations (Input: Accession Number)

    exons_joined=exon_tuples(ac)
    exon_string=[]
    for n in CDS_DNA_string(ac):
        exon_string.append('-')

    for n in range(0,len(exon_string),1):
        for a,b in exons_joined: 
            if n>=(a-1) and n<=b:
                exon_string[n]='*'

    return(exon_string)



def exon_DNA_string(ac):

# Leverages the exon location information to create the CDS DNA string
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




def codons():

# List all amino acid coding codons
    codons=['UUU','UUC','UUA','UUG','AUU','AUC','AUA','AUG','GUU','GUC','GUA','GUG','UCU','UCC','UCA','UCG','CUU','CUC','CUA','CUG','CCU','CCC','CCA',
'CCG','ACU','ACC','ACA','ACG','GCU','GCC','GCA','GCG','UAU','UAC','UAA','UAG','CAU','CAC','CAA','CAG','AAU','AAC','AAA','AAG','GAU','GAC','GAA','GAG',
'UGU','UGC','UGA','UGG','CGU','CGC','CGA','CGG','AGU','AGC','AGA','AGG','GGU','GGC','GGA','GGG'
]
    return(codons)

def chromosome_codons():

# Count codon useage across the CDS DNA String

    total_codon_presence={'UUU':0,'UUC':0,'UUA':0,'UUG':0,'AUU':0,'AUC':0,'AUA':0,'AUG':0,'GUU':0,'GUC':0,'GUA':0,'GUG':0,'UCU':0,'UCC':0,'UCA':0,'UCG':0,'CUU':0,'CUC':0,'CUA':0,'CUG':0,'CCU':0,'CCC':0,'CCA':0,
    'CCG':0,'ACU':0,'ACC':0,'ACA':0,'ACG':0,'GCU':0,'GCC':0,'GCA':0,'GCG':0,'UAU':0,'UAC':0,'UAA':0,'UAG':0,'CAU':0,'CAC':0,'CAA':0,'CAG':0,'AAU':0,'AAC':0,'AAA':0,'AAG':0,'GAU':0,'GAC':0,'GAA':0,'GAG':0,
    'UGU':0,'UGC':0,'UGA':0,'UGG':0,'CGU':0,'CGC':0,'CGA':0,'CGG':0,'AGU':0,'AGC':0,'AGA':0,'AGG':0,'GGU':0,'GGC':0,'GGA':0,'GGG':0}

    for i in getAllEntries():
        rna = transcribe(exon_DNA_string(i['acc']))
        rna_codon = [rna[i:i+3] for i in range(0,len(rna), 3)]
        for i in codons():
            count = rna_codon.count(i)
            total_codon_presence[i]+=count
            
    total_codon_count=sum(total_codon_presence.values())
    
    for i in total_codon_presence:
        total_codon_presence[i]=total_codon_presence[i]/ total_codon_count

    return(total_codon_presence)

def codon_count(ac):

# Return codon useage across the entry and compare to the value for the entire chromosome

    counts=[]
    total_no_codons=len(exon_DNA_string(ac))//3
    rna = transcribe(exon_DNA_string(ac))
    rna_codon = [rna[i:i+3] for i in range(0,len(rna), 3)]
    chromosome_codon_percent = chromosome_codons()
    
    for i in codons():
        count = rna_codon.count(i)
        string = i + ' : ' + str(count) + ' /  ' + str(round((count/total_no_codons)*100,2)) +'% /   ' + str(round((chromosome_codon_percent[i])*100,2)) +'%   '
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



aa={'UUU':'F','UUC':'F','UUA':'L','UUG':'L','AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V','UCU':'S','UCC':'S','UCA':'S','UCG':'S','CUU':'P','CUC':'L','CUA':'L','CUG':'L','CCU':'P','CCC':'P','CCA':'P',
'CCG':'P','ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A','UAU':'Y','UAC':'Y','UAA':'STOP','UAG':'STOP','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
'UGU':'C','UGC':'C','UGA':'STOP','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}



def aa_alignment_string(ac):
    
    # create the animo acid string

    total_no_codons=len(exon_DNA_string(ac))//3
    rna = transcribe(exon_DNA_string(ac))
    rna_codon = [rna[i:i+3] for i in range(0,len(rna), 3)]
    aa_string=[]

    for i in rna_codon:
        try:
            aa_string.append(aa[i])
        except:
            aa_string.append('X')
          

    # align the animo acid string to the CDS string

    protein_mapping=[]
    x=0
    aa_count=0
    exon_binary=exon_string(ac)
    for i in range(0,len(exon_binary),1):

        if exon_binary[i]=='*'and x==0:
            try:
               protein_mapping.append(aa_string[aa_count])
               x+=1
               aa_count+=1       
            except:
               pass
        elif exon_binary[i]=='*'and x==1:
            protein_mapping.append('.')
            x+=1
        elif exon_binary[i]=='*'and x==2:
            protein_mapping.append('.')
            x=0
        
        else:
            protein_mapping.append('-')

    return(protein_mapping)               






