a = True
i,f1,f2,f3 = 0,0,0,1
while a is True:
	if f2 > 0:
		f3 = f1+f2
	f1 = f2
	f2 = f3
	i +=1
	if len(str(f3)) >= 1000:
		a = False
		print(i)
#complete