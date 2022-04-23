#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
filename = '/Users/Denzel/Documents/Birkbeck/CDS_org.txt' 


# In[ ]:


ac = []
# lines = open(filename,'r').readlines()
# for line in lines:
#     p = re.compile(r'(ACCESSION)[\s]+([A-Z]+[0-9]+)')
#     match = p.search(line)
#     if match:
#         ac.append(match.group(2))
# (/product=")(.*)(")((.|\n)*) (/map=")(.*)(")


# In[ ]:


filename = '/Users/Denzel/Desktop/chrom_CDS_1.txt'
with open(filename,'r') as f:
    file = f.read()
    new_file = file.split('//')
    genID = 0
    for line in new_file:
        accession = re.compile(r'ACCESSION[\s]+([A-Z]+[0-9]+)')
        match_a = accession.search(line)
        match_a_grp = match_a.group(1)
        
        gene = re.compile(r'(product)')
        match_g = gene.search(line)
        match_g_grp = match_g.group(1)
        
        if match_a:
            genID += 1
            temp = [genID,match_a_grp,match_g_grp]
            ac.append(temp)


# In[ ]:


print(ac)


# In[195]:


filename = '/Users/Denzel/Desktop/chrom_CDS_1.txt'

re_list = ['ACCESSION[\s]+([A-Z]+[0-9]+)','product="(.*)"', 'gene="(.*)"', 'map="(.*)"']
matches_full = []


with open(filename,'r') as f:
    file = f.read()
    new_file = file.split('//\n')
    genID = 0
for line in new_file:
    genID += 1
    matches = [genID]
    for r in re_list:
        match = re.findall(r,line)
        if match:
            matches.append(match[0])
        else:
            matches.append('N/A')
    matches_full.append(matches)


# In[196]:


print(matches_full)


# In[ ]:




