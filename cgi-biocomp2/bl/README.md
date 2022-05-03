Biocomputing II / cgi-biocomp2/bl
=================================

*TL;DR This folder contains the Business Logic API script, along with full API documentation and reflective essay (Stored in the docs folder)

The function of the Business Logic Layer is to transform data from the DB layer and present it to the Front End to meet the requirements of the genome browser.

Note: The final bl api file is blapi_dummy.py

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
| V10 | Updated API file with documentation [ Current working Version blapi_dummy] |


