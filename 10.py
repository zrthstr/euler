#!/usr/bin/env python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

found = [2]

def smallest_prime(i):
    for n in found:
        if n ** 2 > i:
            found.append(i)
            return i
        if not i % n:
            return n

maxi = 2*10**6

check = 3
while True:
    if (check-1) % 10000:
        print "."
    smallest_prime(check)
    if check > maxi:
        break
    check += 2 
    
print found
prime_sum = 0
for e in found:
    prime_sum += e

print prime_sum

