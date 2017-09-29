from itertools import permutations,islice
def nth_permutation(seq,n):
    return ''.join(next(islice(permutations(seq),n-1,n)))
print(nth_permutation('0123456789',1000000))