Biocomputing II / cgi-biocomp2/bl
=================================
TEST
*TL;DR This folder contains the Business Logic API script, along with full API documentation and reflective essay (Stored in the docs folder)

The function of the Business Logic Layer is to transform data from the DB layer and present it to the Front End to meet the requirements of the genome browser.

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

 
Prerequisites:The functions of this API are dependant on the import of the Regex library, and the db api file in the project directory.


A summary of all the functions available in this API: 

# ENTITIY SPECIFIC ATTRIBUTE EXTRACTION FUNCTIONS


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


# ENTITIY SPECIFIC ATTRIBUTE TRANSFORMATION FUNCTIONS



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
	(Type: string)
      Example Output: 
	
	'['-','-','-''-','-','*','*','*','*','-','-','-','-','-','-',]'

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














 
