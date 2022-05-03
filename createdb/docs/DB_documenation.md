_This file contains all information needed, for the user to understand how the python script is parsing information from the genbank file, in order to populate the database._

### Author: Denzel Eggerue
## Version: 1

A simple import command; Pandas and Regex are both used to extensively to create the database. 
```
import pandas as pd
import re

```

Storing the required details of each genbank entry, in a list (matches_full). The empty list 'recordAll' is used to store the origin sequence separately, where it is later appended into the 'matches_full'. This is done to save time, as it takes too long with regex.
```
filename = 'chrom_CDS_1.txt'

re_list = ['ACCESSION[\s]+([A-Z]+[0-9]+)','product="(.*)"','gene="(.*)"','map="(.*)"','translation="(.*)"','CDS[\s]+([\s\S]*?)gene']

matches_full = []

recordAll = []


with open(filename) as file:
    for record in SeqIO.parse(file, "genbank"):
        recordAll.append(record.seq)
        
recordAll.append(' ')

with open(filename,'r') as f:
    file = f.read()
    new_file = file.split('//\n')
    genID = -1
    
for line in new_file:
    genID += 1
    matches = [genID]
    for r in re_list:
        match = re.findall(r,line)
        if match:
            matches.append(match[0])
        else:
            matches.append('N/A')
    matches.append(recordAll[genID])
    matches_full.append(matches)


print(len(matches_full))
```

The list of details (matches_full) from the genbank file is then separated into individual lists; these lists will form the columns of the pandas dataframe that will be used to create the SQL table. 

```
col_accession = []
col_product = []
col_gene = []
col_chrloc = []
col_AA = []
col_CDS = []
col_origin = []
col_complement = []

for i in matches_full:
    col_accession.append(i[1])
    col_product.append(i[2])
    col_gene.append(i[3])
    col_chrloc.append(i[4])
    col_AA.append(i[5])
    col_CDS.append(i[6])
    col_origin.append(i[7])
    col_complement.append("")

print(col_origin[0])
```

A dataframe is created using the aforementioned lists. Each list represents a column in the dataframe. 

```
df = pd.DataFrame({'Accession Number':col_accession, 'Protein Name':col_product, 'Gene':col_gene, 'Chromosome Location':col_chrloc, 'AA Coding Seq':col_AA,'Complement':col_complement, 'CDS':col_CDS, 'Origin':col_origin})
```
A new column in the data frame is made called 'complement', and is denoted by a 0 or 1. If an entry has a '1' in complement, the coding region sequence is in reverse, if it is a 0 the sequence is not in reverse. This is done to make sure each entry refers to the forward strand and can correctly align with the amino acid sequence.

```
x = 0
for i in df['CDS']:
    if 'complement' in i:
        df.xs(x)['Complement']=1
    else:
        df.xs(x)['Complement']=0
    x+=1
print(df)
```
The "annotations" are removed before the CDS to make it easier to parse.
```
df.replace('complement','', regex = True, inplace = True)
print(df['CDS'])

df.replace('join','', regex = True, inplace = True)
print(df['CDS'])

df.replace('>','', regex = True, inplace = True)
print(df['CDS'])

df.replace('<','', regex = True, inplace = True)
print(df['CDS'])
```
A new column called "Joins" is made in the dataframe; this makes it easier to identify the exons in the Origin DNA sequence. 
```
pattern = '([0-9]+\.\.[0-9]+)'

list_joins = []

for join in df['CDS']:
    match_2 = re.findall(pattern,join)
    list_joins.append(match_2)

df['Joins'] = list_joins
```
This column is dropped since it is replaced by joins.

```
df.drop(['CDS'], inplace = True, axis = 1)
```
A connection is made to the sql server, and a table is initialised with the same columns found in the dataframe.
```
%load_ext sql
%sql mysql+pymysql://ed001:w3jatiunb@localhost/ed001?local_infile=1

%%sql
DROP TABLE IF EXISTS chromosome_1;

CREATE TABLE chromosome_1
(   accession_num   VARCHAR(255)   NOT NULL, 
    protein_name    VARCHAR(255)   NULL, 
    gene            VARCHAR(255)   NULL,
    chromosome_loc  VARCHAR(255)   NULL,
    aa_coding_seq   VARCHAR(255)   NULL,
    complement      CHAR(1)        NULL,
    origin          TEXT           NULL,
    joins           VARCHAR(255)   NULL,
    PRIMARY KEY    (accession_num)
);

SHOW tables;
```
The dataframe is converted into a .csv file, which is then used to insert data into the SQL database. 
```
df.to_csv(r'CDS_sql.csv', header=True, index=None, sep='|', mode='a')

%%sql
LOAD DATA LOCAL INFILE 'CDS_sql.csv'
INTO TABLE chromosome_1
FIELDS TERMINATED BY '|';

%%sql 
SELECT * FROM chromosome_1 LIMIT 10;
```

This code block makes the SQL database Python-friendly / readable by Python, to be used by the business logic layer.
```
import pymysql.cursors

dbname = 'ed001'
dbhost = 'localhost'
dbuser = 'ed001'
dbpassword = 'w3jatiunb'

sql = 'select * from chromosome_1 LIMIT 10'

db = pymysql.connect(host=dbhost, user = dbuser, db = dbname, passwd = dbpassword)

cursor = db.cursor()
nrows = cursor.execute(sql)

l=[]

for row in cursor:
    d={}
    acc=row[0]
    d['acc']=acc
    ppn=row[1]
    gene_id=row[2]
    chrom_loc=row[3]
    CDS_aa_string=row[4]
    CDS_DNA_string=row[5]
    
    l.append(d)
    
print(l)
```

Any entries without a coding region are then removed.
```
%%sql
DELETE FROM chromosome_1
WHERE joins like "[]";

%%sql
SELECT joins FROM chromosome_1 LIMIT 50;
```





