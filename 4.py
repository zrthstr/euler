#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import itertools


def smallest_prime(i):
    for n in range(2,i+1):
        if not i % n:
            #if n * n > i: return i  # speed fiz, should, work. Must be tested though
            return n
        

def facter(i):
    primes = []
    while True:
        sp = smallest_prime(i)
        primes.append(sp)
        if sp == i:
            return primes
        i = i / sp 
    

def facter_count(facters):
    maxf = []
    foo = max(list(itertools.chain(*facters))) # find bigest of all facters
    for c in range( foo ):
        maxf.append(0)
        for f in facters:
            cur = f.count(c+1)
            if cur >= maxf[c]:
                maxf[c] = cur 
    return maxf


facters = [facter(e) for e in range(2,20) ]
print facters
   
multiples = [ c ** m for c, m in enumerate(facter_count(facters),start=1)]

#print multiples

print reduce(lambda x, y: x * y, multiples)




