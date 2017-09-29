from decimal import *
a = 0
getcontext().prec = 102
for i in range(100):
	if (i != 0 and i != 1 and i != 4  and i != 9 and i != 16 and i != 25 and i != 36 and i != 49 and i != 64 and i != 81):
		h = list(str(Decimal(i).sqrt()).replace(".","")[:100])
		for r in range(len(h)):
			a += int(h[r])
print(a)