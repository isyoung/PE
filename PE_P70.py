from sympy import totient
from collections import Counter

limit = 10000000
b = 0
c = limit

def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

r = []
a = list(eratosthenes2(5000))

for i in range(len(a)):
	for j in reversed(range(len(a))):
		r.append(a[i]*a[j])

s = list(set(2r))

for i in range(len(s)):
	b = s[i]/totient(s[i])
	if len(str(totient(s[i]))) == len(str(s[i])) and s[i]<limit:
		if Counter(str(totient(s[i]))) == Counter(str(s[i])):
			if b<c:
				print(b, s[i])
				c = b

print(c)