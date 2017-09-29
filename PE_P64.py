import math

def gcd(a, b):
    return a if b==0 else gcd(b, a%b)

def solve(N):
    sqrt_N = math.sqrt(N)
    x = int(sqrt_N)
    a, b = 1, x
    A = [(a, b)]
    while True:
        c = N - b*b

        # simplify a and c
        gcd_ac = gcd(a, c)
        a /= gcd_ac
        c /= gcd_ac

        x = int(a*(sqrt_N+b)/c)
        a, b = c, x*c - a*b

        if (a, b) in A: break
        else: A.append((a, b))
    index_h = A.index((a, b))
    return len(A) - index_h

N = 10000
square = [i*i for i in range(int(math.sqrt(N)) + 3)]
counter = 0
for i in range(2, N+1):
    if i in square: continue
    if solve(i)%2 == 1: counter += 1
print (counter)