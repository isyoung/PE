
UPPER_BOUND = 10 ** 4
NB_TO_CHOOSE = 5

def is_prime(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            return False
        factor += 1
    return True

def is_valid_pair(n, m):
    return is_prime(int(str(n) + str(m))) and is_prime(int(str(m) + str(n)))

prime_list = []
prime = [True] * UPPER_BOUND

for i in range(2, UPPER_BOUND):
    if prime[i]:
        prime_list.append(i)
        for j in range(i + i, UPPER_BOUND, i):
            prime[j] = False

nb_primes = len(prime_list)

def check_comb(nb_chosen, indices):
    if nb_chosen == NB_TO_CHOOSE:
        for i in indices:
            print(prime_list[i], end = " ")
        print()
    start = -1 
    if nb_chosen > 0:
        start = indices[nb_chosen - 1]
    for i in range(start + 1, nb_primes): 
        valid = True
        for j in range(nb_chosen):
            if not is_valid_pair(prime_list[i], prime_list[indices[j]]):
                valid = False
                break
        if valid:
            indices[nb_chosen] = i 
            check_comb(nb_chosen + 1, indices)

indices = [-1] * NB_TO_CHOOSE
check_comb(0, indices)
