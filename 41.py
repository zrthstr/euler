#!/usr/bin/env python3

"""
Pandigital prime
Problem 41￼
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

#global muts
import math
import eulib4

def mutate_all(r):
    r = list(str(r))
    global muts
    muts = []
    mutate([],r)
    mm = []
    for m in muts:
        #tmp = int(''.join(m))
        mm.append(int(''.join(m)))
    return mm


def mutate(l,r):
    for i in range(len(r)):
        left = l[:]
        if len(r) == 1:
            muts.append(left+[r[0]])
            break

        right = r[:]
        this = right[i]
        right.remove(this)
        left.append(this)

        mutate(left, right)
    

def main():
    base = 123.456789
    all_muts = []

    ## geneate all possible mutations
    for n in range(6,0,-1):
        foo = int(base * (10 ** n))
        all_muts.extend(mutate_all(foo))

    max_composite = math.sqrt(123456789) + 1
    primes = eulib4.primes_to(max_composite)
    prime_muts = []

    ## filter out composite numbers
    for mut in all_muts:
        for p in primes:
            if mut % p == 0:
                break
        else:
            prime_muts.append(mut)

    print("solution: %d", max(all_muts))


if __name__ == "__main__":
    main()
