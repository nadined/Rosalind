
f = open("rosalind_rna.txt", "r")
s = f.read()
f.close()
print s.replace( 'T', 'U')
