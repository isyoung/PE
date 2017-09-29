import sympy
def primetest(a,b,n):
	tf = sympy.ntheory.primetest.isprime(n**2 + a*n + b)
	if  tf == False:
		return False
	if tf == True:
		return True
def primecount():
	h = 0
	for a in range(-1000,1001):
		for b in range(-1000,1001):
			for n in range(100):
				if primetest(a,b,n) == False:
					break
				if primetest(a,b,n) == True:
					if n>h:
						h = n
	return 0
primecount()