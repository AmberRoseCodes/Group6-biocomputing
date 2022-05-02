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

import cgi        # Import the CGI module
import blapi_dummy      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)

form = cgi.FieldStorage()
accession = str(form.getvalue('ac'))
codon_count_table = blapi_dummy.codon_count(accession)
dna_string = blapi_dummy.CDS_DNA_string(accession)
se_string = blapi_dummy.sticky_ends_inplace(accession)
exons = blapi_dummy.exon_string(accession)
amino_acid = blapi_dummy.aa_alignment_string(accession)


html = htmlutils.header()

html += "<h1>Detailed Genbank Results</h1>\n"
html += "  <table>\n"
html += '  <table border="4">\n'


html += "<tr><th style='background-color: yellow' <td>Result of search for Accession Number :  </td>" + "<td>" + accession + "</td></tr>"

html += "<tr><th style='background-color: lightgreen' <td>Protien Product Name: </td>" + "<td>" + blapi_dummy.ppn(accession) + "</td></tr>"  

html += "<tr><th style='background-color: lightblue' <td>Gene ID: </td>" + "<td>"  + blapi_dummy.gene_id(accession) + "</td></tr>"

html += "<tr><th style='background-color: lightpink' <td>Chromosomal Location: </td>" + "<td>"  + blapi_dummy.chrom_loc(accession) + "</td></tr>"

html += "<tr><th style='background-color: lightgrey'<td>CDS AA String: </td>" + "<td>"  + blapi_dummy.CDS_aa_string(accession) + "</td></tr>"

html += "  </table>\n"
html += '  <table border="4">\n'

#dna string details

html += "<h3>CDS DNA String</h3>\n"

html += '  <table>\n'
html += '  <table border="4">\n'

html += '<tr>'
for n in dna_string:
    html += "<td>" + n + "</td>"
html += "</tr>"
html += '<tr>'
for se in se_string:
    html += "<td>" + se + "</td>"
html += "</tr>"
html += '<tr>'
for n in exons:
    html += "<td>" + n + "</td>"
html += "</tr>"
html += '<tr>'
for aa in amino_acid:
    html += "<td>" + aa + "</td>"
html += "</tr>"
html += "  </table>\n"
html += '  <table border="4">\n'


#Codon counting 

html += "<h3>Codon Frequency in CDS DNA String</h3>\n"

html += '<tr>'
x = 0
for codon in codon_count_table:
    if x % 10 == 0:
        html += "</tr>"
        html += "<tr>"
    html += "<td>" + codon + "</td>"
    x += 1
html += "</tr>"
html += "  </table>\n"

html +="Key: <br>"
html +="Count of Codons in genbank entry (1st number)<br>"
html +="Percentage of codons found in this genbank entry (1st percentage)<br>"
html +="Percentage of this codon found in this entire chromsome coding region (2nd percentage)"

html += htmlutils.footer()

print(html)



