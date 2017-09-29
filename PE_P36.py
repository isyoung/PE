from numpy import binary_repr
a = 0
for i in range(1,1000000,2):
	if str(binary_repr(i)) == str(binary_repr(i))[::-1]:
		if str(i) == str(i)[::-1]:
			a+=i
print(a)