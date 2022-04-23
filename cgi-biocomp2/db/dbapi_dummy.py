#!/usr/bin/python3
"""
...Comment header goes here...

This is the database API - it needs to access the MySQL database
"""

# Add the directory above to the module path to import the config file
import sys
sys.path.insert(0, "../")

#import config  # Import configuration information (e.g. database connection)

def getAllEntries():
    import pymysql.cursors

    dbname = 'ed001'
    dbhost = 'localhost'
    dbuser = 'ed001'
    dbpassword = 'w3jatiunb'

    sql = 'select * from chromosome_1 LIMIT 20'

    db = pymysql.connect(host=dbhost, user = dbuser, db = dbname, passwd = dbpassword)

    cursor = db.cursor()
    nrows = cursor.execute(sql)

    l=[]

    for row in cursor:
        d={}
        d['acc']=row[0]
        d['ppn']=row[1]
        d['gene_id']=row[2]
        d['chrom_loc']=row[3]
        d['CDS_aa_string']=row[4]
        d['CDS_DNA_string']=row[5]
        d['joins']=row[6]
        
        l.append(d)
    
    return(l)

    #return([{'acc':'AB000321', 'gene_id':'gh56', 'ppn':'glucoselipid', 'chrom_loc':'103..600','CDS_DNA_string':'test 1 gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg','CDS_aa_string':'test 1 MNRWVEKWLRVYLKCYINLILFYRNVYPPQSFDYTTYQSFNLPQ'},{'acc':'AB000322', 'gene_id':'gkk56', 'ppn':'glucoselipid-2', 'chrom_loc':'203..650','CDS_DNA_String':'test 2 gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg', 'CDS_aa_string':'test 2 MNRWVEKWLRVYLKCYINLILFYRNVYPPQSFDYTTYQSFNLPQ'},{'acc':'AB000323', 'gene_id':'gfdk56', 'ppn':'glucoselipid-3', 'chrom_loc':'403..950','CDS_DNA_String':'test 3 gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg', 'CDS_aa_string':'test 3 MNRWVEKWLRVYLKCYINLILFYRNVYPPQSFDYTTYQSFNLPQ'}])



def codons():
    codons=['uuu','uuc','uua','uug','auu','auc','aua','aug','guu','guc','gua','gug','ucu','ucc','uca','ucg','cuu','cuc','cua','cug','ccu','ccc','cca',
'ccg','acu','acc','aca','acg','gcu','gcc','gca','gcg','uau','uac','uaa','uag','cau','cac','caa','cag','aau','aac','aaa','aag','gau','gac','gaa','gag',
'ugu','ugc','uga','ugg','cgu','cgc','cga','cgg','agu','agc','aga','agg','ggu','ggc','gga','ggg'
]
    return(codons)

def sticky_ends():
    
# Dictionary contains the regognition site for each enzyme, and the index at which it leaves a sticky end on the enzyme, in each case the recognition site is noted from the 5 prime end

    sticky_ends={'EcoRI':['gaattc',0], 'BamHI':['ggatcc',0], 'BsuMI':['acctgc',9]}

    return(sticky_ends)
