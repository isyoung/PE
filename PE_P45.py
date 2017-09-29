tri, pen, hex = [], [], []
n = 1
while True:
	tri.append(n*(n+1)/2)
	pen.append(n*(3*n-1)/2)
	hex.append(n*(2*n-1))
	if tri[-1] in pen and tri[-1] in hex and tri[-1] > 40755:
		print (tri[-1])
		break
	n += 1