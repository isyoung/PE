a = 1
c = 0
for i in range(1,101):
	a *=i
b = str(a)
for r in b:
	c+=int(r)
print(c)