from sympy import totient
b = 0.0
for i in range(1,1000001):
	if (i/totient(i))>b:
		b = i/totient(i)
		print(b,i)
print(b)