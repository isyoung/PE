x = 1
y = 2
z = 0
final = 2
test = True
while test == True:
	z = x+y
	if z % 2 == 0 & z < 4000000:
		final += z
	elif z > 4000000:
		test = False
		break
	x = y
	y = z
print(final)