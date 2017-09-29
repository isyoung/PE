cip=[int(s) for s in open('p059_cipher.txt').read().split(',')]
def cb(k):
	pla=[c^k[i%3] for i,c in enumerate(cip)]
	pl2=''.join(chr(a) for a in pla)
	if ' the ' in pl2:
		print (''.join(chr(a) for a in k), pl2, sum(pla))
[cb([a,b,c]) for a in range(97,123) for b in range(97,123) for c in range(97,123)]