def cal(N):
    a = 1
    for i in range(2,int(N**0.5)+1):
        if N % i  == 0:
            factor1=i
            factor2=N/i
            if factor1==factor2:
                a+=factor1
            else:
                a+= (factor1+factor2)
    if a > N:
        abundant=True
    else:
        abundant=False
    return abundant
number=[]
for i in range(2,28124):
    if cal(i)==True:
        number.append(i)
abundant=[]
for i in number:
    for j in number:
        c=i+j
        if c > 28123 :
            break
        abundant.append(c)
a = list(range(1,28124))
print (sum(range(1,28124)) - sum(set(abundant)))