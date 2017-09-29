total = 100
combinations = [1] + [0]*total
val = []
for i in range(1,100):
	val.append(i)

for x in val:
    for i in range(x,101):
        combinations[i] += combinations[i-x]
print (combinations[total])