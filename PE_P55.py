t = True
a,b = '',''
c,l = 0,0
for i in range(100,10000):
	a = str(i)
	b = a[::-1]
	while t is True:
		a = str(int(a)+int(b))
		b = a[::-1]
		if a == b:
			t = False
		else:
			c+=1
			if c > 50:
				l+=1
				t = False
	c = 0 
	t = True
print(l)