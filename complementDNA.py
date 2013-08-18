f = open("rosalind_revc.txt", "r")
string = f.read()
f.close()

r_string = string[::-1]

def replacer(c):
	if c == 'A':
		return 'T'
	elif c == 'G':
		return 'C'
	elif c == 'C':
		return 'G'
	elif c == 'T':
		return 'A'
	else:
		return c


rr_string = ''.join(map(replacer, r_string))	
print rr_string



