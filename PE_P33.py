from fractions import Fraction

results = []

for i in range(1,10):
	for j in range(1,10):
		for k in range(1,10):
			if i==j or i == k:
				continue
			if (10*i+j)/(10*k+i)==j/k:
				results.append((10*i+j,10*k+i))

frac = Fraction(1,1)

for r in results:
	frac = frac * Fraction(r[1],r[0])

print(frac.denominator)