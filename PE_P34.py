def factorial(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n * factorial(n-1)

def sumOfdigits(n):
	return sum([factorial(int(value)) for value in list(str(n))])

print(sum([i for i in range(3,1000000) if i == sumOfdigits(i)]))