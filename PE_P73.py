from fractions import gcd # just a wrapper of the Fractions gcd implementation

def fracs_in_range(n):
    count = 0
    for i in range(n//3+1,(n//2)+n%2):
        if gcd(i,n) == 1: count += 1
    return count

if __name__ == "__main__":
    print(sum(fracs_in_range(n) for n in range(12001)))