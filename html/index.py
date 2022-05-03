#!/usr/bin/env python3
"""
...Comment header goes here...

# Index.py created by Hirushi Rajapakse for making the front end. Addition of image.titles,description,table styles,footer.
# V3

# biocomp2.css created by Hirushi Rajapakse to point the stylesheet. Aesthetics for body, content and footer layout
#V3

# tried to add a loader but didnt succeed <div class="loader"></div>

Simple script to generate the index.html file so that we can pick up
configuration information from the config file.
"""

# Add the CGI directory which is where the config file lives
import sys
sys.path.insert(0, "../cgi-biocomp2")
import config

print(
"""<!DOCTYPE html>

<!-- A header comment goes here
-->

<html>

  <head>
   <img align="middle" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Ideogram_human_chromosome_1.svg/600px-Ideogram_human_chromosome_1.svg.png" class="center" width="400" height="150">  
   <title>Biocomputing II - framework</title>
    <link rel='stylesheet' type='text/css' href='css/biocomp2.css'/>
  </head>
  
  <body>
    <div class='content'>
      <h1><center>Biocomputing II - Group 6 Database for Chromosome 1</centre></h1>
      <center>The GenBank database allows access to scientific community to retrieve most up-to-date and comprehensive DNA sequence information. This geneome brower will display genbank files associated with chromosome 1</centre></>

      
      </p>


        <a href='""" + config.listallurl + """'>List all entries</a>
      </p>
      
      <form action='""" + config.listallurl + """' method='get'>
      <p> The table below will search and return genes based on Accession Number, Chromosomal Location and Protein products

       
        <p class="center"><b>Search by:</b></p>
        <table border='4'>\n
          <tr>
            <td>Genbank accession</td>
            <td><input type='text' name='ac'/></td>
          </tr>
          <tr>
            <td>Gene identifier</td>
            <td><input type='text' name='gi'/></td>
          </tr>
          <tr>
            <td>Protein product</td>
            <td><input type='text' name='ppn'/></td>
          </tr>
          <tr>
            <td>Chromosomal location</td>
            <td><input type='text' name='loc'/></td>
          </tr>
        </table>

        <p><input type='Submit' value='Search' /></p

      </form>
      
    </div> <!-- content -->
  </body>
</html>

<div class="footer">
         <p>Created by Hirushi, Amber, Denzel and Farah Birkbeck University 2022</p>
        </div>
""")
