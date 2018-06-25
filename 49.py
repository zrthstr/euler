#!/usr/bin/env python3

"""
Prime permutations
Problem 49￼
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import eulib
import collections

# search space
MIN = 1000
MAX = 9999



def is_permutation(a, b):
    a = sorted(list(str(a)))
    b = sorted(list(str(b)))
    return a == b


if __name__ == "__main__":

    primes = [p for p in eulib.fill_prime_list(MAX) if p >= MIN]
    for p in primes:
        for a in range(2, MAX // 3):
            if p + a in primes and p + a + a in primes:
                if is_permutation(p, p+a) and is_permutation(p, p+a+a):
                    print("found candidate: %d (%d), %d , %d" %( p, a, p+a, p +a +a )) 
                    print("--> %d%d%d" %(p,p+a,p+a+a))
