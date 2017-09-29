from fractions import Fraction
from functools import reduce
from itertools import chain, count, islice


def digit_sum(n):
    return sum(map(int, str(n)))


def convergent(terms, n):
    return reduce(lambda acc, x: x + Fraction(1, acc), reversed(list(islice(terms, n))), 1)


def e_convergent(n):
    return convergent(chain([2], chain.from_iterable([1, 2 * k, 1] for k in count(1))), n)


print(digit_sum(e_convergent(99).numerator))