#!/usr/bin/env python3
"""
Python script which generates landing page for the database.

Simple script to generate the index.html file so that we can pick up
configuration information from the config file.
"""

# Add the CGI directory which is where the config file lives
import sys
sys.path.insert(0, "../cgi-biocomp2")
import config

print(
"""<!DOCTYPE html>

<!-- This is the index.html script, Author: Farah Khan, Version: 1, Date: 02/05/2022
-->

<html>

  <head>
    <img align="middle" src="https://chromodisorder.org/wp-content/uploads/2017/11/chromosome-1.png" class="center"/> 
    <title>Biocomputing II - framework</title>
    <link rel='stylesheet' type='text/css' href='css/biocomp2.css' />
  </head>
  
  <body>
    <div class='content'>
      <h1><center>Biocomputing II - Group 6 Database</center></h1>
      <p>An online database containing information for various genes found 
	in Human Chromosome 1.</p>
      
      <p>This database allows you to search for specific genes based on multiple
	parameters including: Accession Number, Chromosomal Location and Protein 	products among others.The results page will return a table of information 	regarding the gene you have searched for. For example, if you search 'RHD' 	in 'Gene ID' the results will show you information only for genes with that 	Gene ID, as well as their accession numbers, protein products etc.
      </p>

      <p><b>Note</b> A table will also be returned for each specific entry, 		highlighting respective codon usage in said entry, as well as across the 	entire database. Upon clicking a specific entry, a more detailed breakdown 	for the search can be seen, with information such as restriction enzyme 		sites. 
      </p>
      
      <p>
        <a href='""" + config.listallurl + """'>List all entries</a>
      </p>
      
      <form action='""" + config.listallurl + """' method='get'>
        <p class="center"><b>Search by:</b></p>
        
        <table class="center">
          <tr>
            <td>Genbank Accession</td>
            <td><input type='text' name='ac'/></td>
          </tr>
          <tr>
            <td>Gene Identifier</td>
            <td><input type='text' name='gi'/></td>
          </tr>
          <tr>
            <td>Protein Product</td>
            <td><input type='text' name='ppn'/></td>
          </tr>
          <tr>
            <td>Chromosomal Location</td>
            <td><input type='text' name='loc'/></td>
          </tr>
        </table>

        <p><input type='Submit' value='Search' /></p>

      </form>
    </div> <!-- content -->
  </body>
</html>
""")
