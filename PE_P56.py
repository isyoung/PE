b = 0
for i in range(2,100):
	for j in range(2,100):
		a = sum(map(int, list(str(i**j))))
		if a>b:
			b = a
print(b)