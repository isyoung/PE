import itertools 
from math import sqrt
keep = 0
hold = 0
for i in itertools.count():
	hold += i
	half = int(hold/2)
	print(hold)
	for k in range(1,half):
		if hold%k == 0:
			keep+=1
			if keep >= 500:
				print(i)
				break
	keep = 0
