import pyprimes

def rightcheck(g):
    if pyprimes.is_prime(g):
        if g<10: return True
        else: return rightcheck(g//10)
    else:
        return False

def leftcheck(g):
    if pyprimes.is_prime(g):
        l.append(g)
        for i in [1,2,3,5,7,9]:
            leftcheck(int(str(i)+str(g)))

l=list()
for i in range(1,10):
    leftcheck(i)
m=[i for i in l if rightcheck(i) and i>10]
print(m)
print(sum(m))