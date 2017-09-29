def findHaupt(b,n):
    e = 1
    while b**e%n!=1:
        e+=1
    return e
maxHaupt = 0
num = 0
for i in range(2,1000):
    if i%2!=0 and i%5!=0:
        haupt = findHaupt(10,i)
        if haupt > maxHaupt:
            num = i
            maxHaupt = haupt
print(num)