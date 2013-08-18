
f = open("rosalind_dna.txt", "r")

str = f.read() 
f.close()

sub1 = 'A'
sub2 = 'C'
sub3 = 'G'
sub4 = 'T'

print str.count(sub1), str.count(sub2), str.count(sub3), str.count(sub4)

#or 
#a_counts = str.count('A')
#c_counts = str.count('C')
#g_counts = str.count('G')
#t_counts = str.count('T')

#print a_counts, c_counts, g_counts, t_counts
