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
html += "<th>Gene ID</th>"
html += "<th>Protien Product Name</th>"
html += "<th>Chromosomal Location</th></tr>\n"

for d in entries:
        html += "<tr><td>" + "<a href='" + config.searchurl + "?ac=" + d.get('acc') + "'>"+ d.get('acc') + "</a>""</td>"
        html += "<td>" + d.get('gene_id')+ "</td>"
        html += "<td>" + d.get('ppn')+ "</td>"
        html += "<td>" + d.get('chrom_loc')+ "</td></tr>"


    
html += "  </table>\n"
html += htmlutils.footer()

print(html)


#<td>Hi, I'm your first cell.</td>
#Copy to Clipboard
#If we want a row of four cells, we need to copy these tags three times. Update the contents of your table to look like so:
#<td>Hi, I'm your first cell.</td>
#<td>I'm your second cell.</td>
#<td>I'm your third cell.</td>
#<td>I'm your fourth cell.</td>

