adval = 1
skip = 1
hold = 0
a = 0
kt = 0
for i in range(2,1002002):
	a = skip - hold
	hold += 1
	if a == 0:
		adval += i
		kt += 1
		hold = 0
		if kt == 4:
			kt = 0
			skip += 2
print(adval)