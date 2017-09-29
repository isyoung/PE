for i in range(100000,100000001):
	print(i)
	for j in range(1,7):
		if set(list(str(i))) - set(list(str(i*j))) == False:
			print(i)
			break