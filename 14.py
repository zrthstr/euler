#!/usr/bin/env python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
import itertools

def step(n):
    if not n % 2:
        return n / 2
    else:
        return 3 * n + 1



chains=[]
chains.append([3,10,5,16,8,4,2])
chains.append([2,1])
chains_flat = []


largest = 0
largest_start = 0

to = 1*10**4
for start in range(to,1,-1):
    new_len = len(flat)

    print "testing:", start,
    new_chain = [start]
#    flat = sum(chains,[])
    if not old_len == new_len:
        flat = list(set(itertools.chain.from_iterable(chains)))
        old_len = len(flat)
    else:
        print "skipping recalc"

    while not start == 1:
        if start in flat:
        #if start in sum(chains,[]):

            chains.append(new_chain)
            print "breaking", start, new_chain
            break
        start = step(start)
        new_chain.append(start)


print chains
#print largest_start, " has ",  largest
