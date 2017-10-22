#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143


def is_prime(i):
	for p in fprimes:
		if not i % p:
			return 0
	else:
		return i


fprimes = []

def primes():
	i = 1
	while True:
		i+=1
		if is_prime(i):
			fprimes.append(i)
			yield i
		

for p in primes():
    if n % p:
        continue
    if n == p:
        print "SOLVED:", n 
        break
    print "reducing", n , "to: ", n / p 
    n = n / p
    while not n % p:  # in case if multiplicate prime
        n = n / p



