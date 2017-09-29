import sympy.ntheory.factor_ as snf
a = 0
for i in range(2,1000001):
	a+= snf.totient(i)
print(a)