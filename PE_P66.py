from math import sqrt

def chakravala(N):
    m,k,a,b = 1,1,1,0
    while k!=1 or b==0:
        m = k*(m/k+1) - m
        m = m - int((m-sqrt(N))/k)*k
        tempA = (a*m + N*b)/abs(k)
        b = (a+b*m)/abs(k)
        k = (m*m-N)/k
        a = tempA
    return (a)
    
x_max,d_max = 0,2
for d in range(2,1001):
    if int(sqrt(d))**2 != d:
        x = chakravala(d)
        if x>x_max:
            x_max,d_max =x,d
print (d_max)