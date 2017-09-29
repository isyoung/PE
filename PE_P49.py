def main(n):
	multiples = set()
	for i in range(2, n+1):
		if i not in multiples:
			yield i
			multiples.update(range(i*i, n+1, i))
	r = list(multiples)
	for t in range(1,len(r)):
		s = (2*r[t-1] + r[t])
		if s < 10000 and s in r:
			if sorted(str(r[t])) == sorted(str(r[t-1])) == sorted(str(s)):
				print (t-1,t,r)
	return -1

main(10000)