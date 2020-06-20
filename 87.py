#!/usr/bin/env python3

'''
Prime power triples
￼  ￼  ￼
Problem 87
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''

import eulib4
import math

def main():
    MAX = 50000000

    found = set()
    for a in [p ** 2 for p in eulib4.primes_to(MAX**(1./2.))]:
        for b in [p ** 3 for p in eulib4.primes_to(MAX**(1./3.))]:
            for c in [p ** 4 for p in eulib4.primes_to(MAX**(1./4.))]:
                s = a + b + c
                if s < MAX:
                    found.add(s)

    print(len(found))

if __name__ == "__main__":
    main()
