#!/usr/bin/python3
"""
...Comment header goes here...

This CGI script obtains all the entries from the BL layer and formats them for 
HTML display as a table
"""

# Add the bl sub-directory to the module path
# And the directory above to import the config file
import sys
sys.path.insert(0, "../bl/")
sys.path.insert(0, "../")

import blapi_dummy      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)
import cgi

form = cgi.FieldStorage()
ac = str(form.getvalue('ac'))
gi = str(form.getvalue('gi'))
ppn = str(form.getvalue('ppn'))
loc = str(form.getvalue('loc'))

entries = blapi_dummy.getAllEntries()
html    = htmlutils.header()

html += "  <table>\n"
html += '  <table border="4">\n'
html += "<tr><th style='background-color: yellow'>Accession Number</th>"
html += "<th style='background-color: lightgreen'>Gene ID</th>"
html += "<th style='background-color: lightblue'>Protien Product Name</th>"
html += "<th style='background-color: lightpink'>Chromosomal Location</th></tr>\n"



if 'ac' not in form and 'gi' not in form and 'ppn' not in form and 'loc' not in form:
        for d in entries:
                html += "<tr><td>" + "<a href='" + config.searchurl + "?ac=" + d.get('acc') + "'>"+ d.get('acc') + "</a>""</td>"
                html += "<td>" + d.get('gene_id')+ "</td>"
                html += "<td>" + d.get('ppn')+ "</td>"
                html += "<td>" + d.get('chrom_loc')+ "</td></tr>"


if 'ac' in form:
        for d in entries:
                if d.get('acc') == ac:
                        html += "<tr><td>" + "<a href='" + config.searchurl + "?ac=" + d.get('acc') + "'>"+ d.get('acc') + "</a>""</td>"
                        html += "<td>" + d.get('gene_id')+ "</td>"
                        html += "<td>" + d.get('ppn')+ "</td>"
                        html += "<td>" + d.get('chrom_loc')+ "</td></tr>"

elif 'gi' in form:
        for d in entries:
                if d.get('gene_id') == gi:
                        html += "<tr><td>" + "<a href='" + config.searchurl + "?ac=" + d.get('acc') + "'>"+ d.get('acc') + "</a>""</td>"
                        html += "<td>" + d.get('gene_id')+ "</td>"
                        html += "<td>" + d.get('ppn')+ "</td>"
                        html += "<td>" + d.get('chrom_loc')+ "</td></tr>"

elif 'ppn' in form:
        for d in entries:
                if d.get('ppn') == ppn:
                        html += "<tr><td>" + "<a href='" + config.searchurl + "?ac=" + d.get('acc') + "'>"+ d.get('acc') + "</a>""</td>"
                        html += "<td>" + d.get('gene_id')+ "</td>"
                        html += "<td>" + d.get('ppn')+ "</td>"
                        html += "<td>" + d.get('chrom_loc')+ "</td></tr>"
elif 'loc' in form:
        for d in entries:
                if d.get('chrom_loc') == ppn:
                        html += "<tr><td>" + "<a href='" + config.searchurl + "?ac=" + d.get('acc') + "'>"+ d.get('acc') + "</a>""</td>"
                        html += "<td>" + d.get('gene_id')+ "</td>"
                        html += "<td>" + d.get('ppn')+ "</td>"
                        html += "<td>" + d.get('chrom_loc')+ "</td></tr>"
                 
html += "  </table>\n"
html += htmlutils.footer()

print(html)



