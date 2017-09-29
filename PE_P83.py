import bisect

m = [[int(s) for s in line.strip().split(',')] for line in open('data/p083_matrix.txt')]
seen = dict()
q = [(m[0][0],0,0)]
for val,i,j in q:
	if i==j==len(m)-1:
		print(val)
		break
	for _i,_j in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
		if _i in range(len(m)) and _j in range(len(m)) and (_i,_j) not in seen:
			bisect.insort(q, (val+m[_i][_j], _i, _j))
			seen[(_i,_j)] = 1