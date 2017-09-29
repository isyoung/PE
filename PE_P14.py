a=0
b=0
c=0
d=0
def collatz(n):
	if n%2 == 0:
		n/=2
	else:
		n = 3*n+1
	return n

for i in range(2,1000001):
	b = collatz(i)
	while b!=1:
		b = collatz(b)
		a+=1
		if a > c:
			c = a
			d = i
	a = 0
	b = 0
print("Finished, number = ", d, "Number of iterations = ", c)