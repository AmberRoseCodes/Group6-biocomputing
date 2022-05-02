#!/usr/bin/env python3
"""
...Comment header goes here...

# Index.py created by Hirushi Rajapakse for making the front end
# V1

#biocomp2.css created by Hirushi Rajapakse to point the stylesheet
#V1

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
   <img src='https://www.thoughtco.com/thmb/CxJQOpWm1-rSrktSijLtIVEjGXg=/768x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/chromosomes-567300453df78ccc15fd3c19.jpg' width="150" height="150"> 
    <link rel='stylesheet' type='text/css' href='css/biocomp2.css'/>
  </head>
  
  <body>
    <div class='content'>
      <h1>Biocomputing II Group 6 Chromosome 1 <centre> </h1>
      <p> The GenBank database allows access to scientific community to retrieve most up-to-date and comprehensive DNA sequence information. This geneome brower will display genbank files associated with chromosome 1.</p> 

      </p>

      <p>
        <a href='""" + config.listallurl + """'>List all entries</a>
      </p>
      
      <form action='""" + config.listallurl + """' method='get'>
        <p>Search by:</p>
        
      <div class='table'>
        <table>
        <table border='4'>\n'
          <tr>
            <td>genbank accession</td>
            <td><input type='text' name='ac'/></td>
          </tr>
          <tr>
            <td>gene identifier</td>
            <td><input type='text' name='gi'/></td>
          </tr>
          <tr>
            <td>protein product</td>
            <td><input type='text' name='ppn'/></td>
          </tr>
          <tr>
            <td>chromosomal location</td>
            <td><input type='text' name='loc'/></td>
          </tr>
        </table>

        <p><input type='Submit' value='Search' /></p>

      </form>
    </div> <!-- content -->
  </body>
</html>
""")
