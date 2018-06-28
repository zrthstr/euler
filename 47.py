#!/usr/bin/env python3

"""
Distinct primes factors
Problem 47￼
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

import eulib4

def main():
    START = 99
    
    # number of consecutive matches needed
    CONSEC_N = 4

    # primes needed for factorisation to be a match
    CONSEC_P = 4


    found = 0
    test = START

    while found < CONSEC_N:
        test +=1
        uniq = eulib4.uniq_factors(test)

        if len(uniq) == CONSEC_P:
            found += 1
        else:
            found = 0

        print(test, ">", uniq, ":", found)

    result = test - CONSEC_N  + 1
    print("Found: %d" % result)

if __name__ == "__main__":
    main()
