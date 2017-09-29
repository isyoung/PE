import math

def is_prime(n):
    if n == 2:
        return True
    for num in range(2, int(math.sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True

def is_circular_prime(num):
    strnum = str(num)
    for i in range(1, len(strnum)):
        strnum = strnum[1:] + strnum[0]
        if not is_prime(int(strnum)):
            return False
    return True

summ = 0
for num in range(2, 1000000):
    if is_prime(num):
        if is_circular_prime(num):
            summ += 1

print(summ)