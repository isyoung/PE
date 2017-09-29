from math import factorial
count=0
for n in range(1,1000000):
    list=[n]
    new=sum([factorial(int(i)) for i in str(n)])
    while new not in list:
        list+=[new]
        new=sum([factorial(int(i)) for i in str(new)])
    if len(list)==60:count+=1
print(count)