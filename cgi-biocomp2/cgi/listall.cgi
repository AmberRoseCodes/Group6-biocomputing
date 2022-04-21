#!/usr/bin/python3
"""
...Comment header goes here...

This CGI script obtains all the entries from the BL layer and formats them for 
HTML display as a table
"""

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "../bl/")
sys.path.insert(0, "../")

import blapi_dummy      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)

entries = blapi_dummy.getAllEntries()
html    = htmlutils.header()

html += "  <table>\n"
html += "<tr><th style='background-color: yellow'>Accession Number</th>"
html += "<th style='background-color: green'>Gene ID</th>"
html += "<th style='background-color: red'>Protien Product Name</th>"
html += "<th style='background-color: blue'>Chromosomal Location</th></tr>\n"

for d in entries:
        html += "<tr><td>" + "<a href='" + config.searchurl + "?ac=" + d.get('acc') + "'>"+ d.get('acc') + "</a>""</td>"
        html += "<td>" + d.get('gene_id')+ "</td>"
        html += "<td>" + d.get('ppn')+ "</td>"
        html += "<td>" + d.get('chrom_loc')+ "</td></tr>"


    
html += "  </table>\n"
html += htmlutils.footer()

print(html)



