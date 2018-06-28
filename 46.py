#!/usr/bin/env python3


"""
Goldbach's other conjecture
Problem 46￼
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import eulib4
from math import sqrt


def goldbach2(n):
    # list of primes for reverence
    # rm '2' as this would make composit_rests uneven and thus cant be the solution
    primes = eulib4.primes_to(n-1)[1:]

    for p in primes:
        half_rest = (n - p ) // 2 
        if int(sqrt(half_rest))**2 == half_rest:
            #print("ok.. %d = %d + 2x%d" %(n, p, half_rest))
            return True
    return False


def main():
    ## we know from the question that there is no solution below 34
    test = 33
    PrimeGen = eulib4.prime_gen()
    primes = [PrimeGen.__next__()]

    while True:
        if primes[-1] < test:
            primes.append(PrimeGen.__next__())   
            continue
        if test not in primes:
            if not goldbach2(test):
                print("solution: %d" % test)
                break

        ## we are only looking for odd composites
        test +=2
        

if __name__ == "__main__":
    main()
