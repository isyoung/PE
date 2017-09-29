total = 200
combinations = [1] + [0]*total
val = [1,2,5,10,20,50,100,200]
for x in val:
    for i in range(x,201):
        combinations[i] += combinations[i-x]
print (combinations[total])