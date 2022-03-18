from distutils.file_util import write_file


filename = '/Users/Denzel/Documents/Birkbeck/Group6-biocomputing/chrom_CDS_1.txt'
with open(filename,'r') as f:
    file = f.read()
    new_file = file.split('//')
    with open('organised_file.txt','w')as nf:
        for line in new_file:
            nf.write(line + "\n" + "------------------------------------------------------------------------------------------" + "\n")