from fractions import gcd
m,n,maxL=2,1,1500000
g,b=set(),set()
while 2*m**2+2*m < maxL+1:
	while n<m:
		if gcd(n,m) == 1 and (m - n) % 2 == 1:
			L = 2*m**2+2*m*n
			k = 1
			while k*L<maxL+1:
				if k*L in g:b |= {k*L}
				else: g|={k*L}
				k+=1
		n+=1
	m+=1
	n=1
print(len(g-b))