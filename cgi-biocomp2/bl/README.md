Biocomputing II / cgi-biocomp2/bl
=================================

*TL;DR this file provides the **API Doucmentation**, giving the user the necessary information to use and understand the functions contained within the API*

**Author: Amber Hilton**

**Date: 02/05/2022**

| Version | Description |
| --- | ----------- |
| V1  | Established the Dummy API code |
| V2  | Updated the Dummy API code following design itteration |
| V3  | Created Variable functions to return entity specific variables |
| V4  | Created Sticky End Fucntions |
| V5  | Created entity codon count Functions |
| V6  | Created String functions to align Sticky Ends and Exons to the full origin sequence| 
| V7  | Created translate and transcribe functions and function to stich exon DNA regions together |
| V8  | Updated functions to point at Exon DNA region rather than Full origin sequence where required |
| V9  | Updated codon count Functions to include full chromosome % and entity specific %  |
| V10 | Updated API file with documentation [ Current working Version ] |



This page describes the structure of the Business Logic API paths and operations and how they can be used to access and manage data.

The raw data is extracted from the DB layer by calling a function in the DB API, this returns the data in a list of dictionaries, each dictionary representing a row in the database - getAllEntries()

The majority of all other functions defined in this API are dependant on this initial Ddata Access API.The other functions are broken into to main categories; Extraction and Transformation. The functions have been defined by the user journeys provided in the original project brief, but can be comibed and used to enhance functionality beyond what is demonstrated in this project submission. 

 
API Prerequisites: The functions of this API are dependant on the import of the Regex library, and the db api file in the project directory.


## A summary of all the functions available in this API: 

### ENTITIY SPECIFIC ATTRIBUTE EXTRACTION FUNCTIONS


getAllEntries()  

      INPUT: None 
	(Type: N/A)
      OUTPUT: List of dictionaries, each dictionary representing a row in the DB populated from the genbank file for CHromosome 1
	(Type: List of Dictionaries)
      Example Output: 

	[{'acc': 'AB000360', 
	'ppn': 'N/A', 
	'gene_id': 'PIGC', 
	'chrom_loc': '1q23-q25', 
	'CDS_aa_string': 'N/A', 
	'complement': '0', 
	'CDS_DNA_string': 'GGATCCCAGCTCCAGCACTGACACCATCTATGCCATGTCAGTCTT', 
	'joins': "['1101..1994']"},
	{'acc': 'AB003474', 
	'ppn': 'N/A', 
	'gene_id': 'STK6P', 
	'chrom_loc': '1q41-q42', 
	'CDS_aa_string': 'N/A', 
	'complement': '0', 
	'CDS_DNA_string': 'AAGACTTTGAAATTGGTCGCCCTCCGGGTAAAGGAAAGTTTGG', 
	'joins': "['1..915']"}
	... etc.]


getAnEntry(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single dictionary representing a row in the DB that corresponds to the Input Accession Number from the genbank file
	(Type: Dictionary)
      Example Output: 

	{'acc': 'AB000360', 
	'ppn': 'N/A', 
	'gene_id': 'PIGC', 
	'chrom_loc': '1q23-q25', 
	'CDS_aa_string': 'N/A', 
	'complement': '0', 
	'CDS_DNA_string': 'GGATCCCAGCTCCAGCACTGACACCATCTATGCCATGTCAGTCTT', 
	'joins': "['1101..1994']"}

gene_id(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single value for the gene identification that corresponds to the Input Accession Number from the genbank file
	(Type: string)
      Example Output: 
	
	'STK6P'

ppn(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single value for the protein product name that corresponds to the Input Accession Number from the genbank file
	(Type: string)
      Example Output: 
	
	'Rh blood group antigen'


chrom_loc(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single value for the protein product name that corresponds to the Input Accession Number from the genbank file
	(Type: string)
      Example Output: 
	
	'Rh blood group antigen'


CDS_aa_string(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single value for the Amino Acid string that corresponds to the Input Accession Number from the genbank file
	(Type: string)
      Example Output: 
	
	'MAPVKKLVVKGGKKKKQVLK'


joins(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single value for the locations of the exomes that corresponds to the Input Accession Number from the genbank file
	(Type: string)
      Example Output: 
	
	'['22..33', '1840..1887']'

      Note: this is later transformed using the function exon_tuples(ac)


complement(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single value for the locations of the exomes that corresponds to the Input Accession Number from the genbank file
	(Type: string)
      Example Output: 
	
	'1'

      Note: this is used in the CDS_DNA_string function to flag any entries which need translation due to the record being recorded as a reverse strand. 



CDS_DNA_string(ac)

      INPUT: Accession Number (eg. AB000360)
	(Type: string)
      OUTPUT: Single value for the full CDS origin DNA sequence that corresponds to the Input Accession Number from the genbank file. If the entry is flagged as a reverse strand record the DNA is translated before ebing returned so that each entry represents the forward strand.
	(Type: string)
      Example Output: 
	
	'AAGCTTGTGGTGAAGGGGGGCAAAAAAAAGAAGCAAGTTCTGAAG'

      Note: This string is later transformed to produce a DNA string containing only the coding regions, see exon_DNA_string(ac). It also uses the transform function translate(DNA).


### ENTITIY SPECIFIC ATTRIBUTE TRANSFORMATION FUNCTIONS



translate(DNA)

	INPUT: DNA (eg. AAGCT)
	(Type: string)
	OUTPUT: DNA reverse complimented
	(Type: string)
      Example Output: 
	
	'TTCGA'

exon_tuples(ac)

	INPUT: Accession Number (eg. AB000360)
	(Type: string)
	OUTPUT: join data in the form of a list of tuples. Representing the start and end locations of each exon in a genbank entry.
	(Type: list of tuples)
      Example Output: 
	
	'[(100,200),(300,400)]'


exon_string(ac)

	INPUT: Accession Number (eg. AB000360)
	(Type: string)
	OUTPUT: A list the length of the full origin CDS DNA string, denoting with a * where the exons are located. 
	(Type: list)
      Example Output: 
	
	['-','-','-''-','-','*','*','*','*','-','-','-','-','-','-',]

	Note: Exon location is identified using the function exon_tuples(ac)


exon_DNA_string(ac)

	INPUT: Accession Number (eg. AB000360)
	(Type: string)
	OUTPUT: A concatenated string containing the DNA from only the exons in seqeuntial order
	(Type: string)
      Example Output: 
	
	'AAGCTTGTGGTGAAGGGGGGCAAAAAAAAGAAGCAAGTTCTGAAG'

	Note: Exon location is identified using the function exon_tuples(ac)


transcribe(DNA)


	INPUT: Accession Number (eg. AB000360)
	    (Type: string)
	OUTPUT: A concatenated string containing the DNA from only the exons in seqeuntial order
	(Type: string)
     		 Example Output: 
	
	'AAGCTTGTGGTGAAGGGGGGCAAAAAAAAGAAGCAAGTTCTGAAG'

	Note: Exon location is identified using the function exon_tuples(ac)


codons()


	INPUT: None
	    (Type: N/A)
	OUTPUT: A list of all codons that exist
      (Type: List of strings)
     		 Example Output: 
	
	['UUU','UUC','UUA','UUG','AUU','AUC','AUA','AUG','GUU','GUC','GUA','GUG','UCU','UCC','UCA','UCG','CUU','CUC','CUA','CUG','CCU','CCC']

	Note: This is additional data required for transformations that is not provided by the genbank file


chromosome_codons()

	INPUT: None
	    (Type: N/A)
	OUTPUT: A dictionary of all possible codons which code for amino acids, and their presence across all coding regions of Chromosome 1
      (Type: Dictionary)
     		 Example Output:
         
         {'UUU': 0.024455077086656035, 'UUC': 0.02073365231259968, 'UUA': 0.012227538543328018}

	Note: This count takes into consideration exons only and provides a count across all entries in the DB


codon_count(ac)

	INPUT: Accession Number (eg. AB000360)
	    (Type: string)
	OUTPUT: A list of strings containing a mixture of text and data collected from various functions to display the codon count and % statistics
	(Type: string)
     		 Example Output: 
	      ['UUU : 0 /  0.0% /   2.45%   ', 'UUC : 0 /  0.0% /   2.07%   ', 'UUA : 0 /  0.0% /   1.22%   ', 'UUG : 0 /  0.0% /   1.14%   ', 'AUU : 0 /  0.0% /   1.67%   ', 'AUC : 0 /  0.0% /   1.33%   ', 'AUA : 0 /  0.0% /   0.8%   ', 'AUG : 1 /  5.0% /   1.59%   ', 'GUU : 1 /  5.0% /   1.3%   ', 'GUC : 0 /  0.0% /   1.44%   ', 'GUA : 0 /  0.0% /   0.74%   ', 'GUG : 3 /  15.0% /   1.81%   ', 'UCU : 0 /  0.0% /   1.59%   ', 'UCC : 0 /  0.0% /   1.83%   ', 'UCA : 0 /  0.0% /   1.62%   ]

	Note: The format of this string has been developed specifically for the intended presentation in the front end


sticky_ends()

	INPUT: None
	    (Type: N/A)
	OUTPUT: A dictionary containing information about restriction enzymes and their recognition patterns (nucleotide bases which the enzymes will cut on the DNA string)
	(Type: dictionary)
     		 Example Output:
         
         {'EcoRI':['GAATTC',0], 'BamHI':['GGATCC',0], 'BsuMI':['ACCTGC',9]}

	Note: This is additional data required for transformations that is not provided by the genbank file
  

sticky_ends_loc(ac,enzyme)

	INPUT: Accession Number (eg. AB000360), Enzyme (eg. 'EcoRI')
	    (Type: string / string)
	OUTPUT: A list containing the locations the enzyme regognition patterns from the sticky_ends() dictionary is located for a specific enzyme for a specific genbank entry according to its accession number
	(Type: list of int)
     		 Example Output:
         
         [2576,3567]

sticky_ends_inplace(ac)

	INPUT: Accession Number (eg. AB000360)
	    (Type: string)
	OUTPUT: A list the length of the full origin CDS DNA string, denoting with with Restriction Enzyme name where the recognition pattern is identified in the CDS DNA string 
	(Type: list)
     		 Example Output:
         
         ['-','-','-''-','-','EcoRI','-','-','-','-','-','BsuMI','-','-','-',]
         
         	Note: The format of this string has been developed specifically for the intended presentation in the front end
          
aa_alignment_string(ac)

	INPUT: Accession Number (eg. AB000360)
	    (Type: string)
	OUTPUT: A list the length of the full origin CDS DNA string, aligning the amino acid to the codon within the exon regions. The Amino Acid is noted as a single letter followed by two dots, where a codon is made up of three nucelotide bases and codes for a single amino acid. 
	(Type: list)
     		 Example Output:
         
         ['-','-','-''-','-','A','.','.','H','.','.','G','.','.','-',]
         
         	Note: The format of this string has been developed specifically for the intended presentation in the front end
          


