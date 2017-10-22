#!/usr/bin/env python

"""
What is the 10 001st prime number? 
"""

found = [2]

def smallest_prime(i):
    for n in found:
        if n ** 2 > i:
            found.append(i) 
            return i  
        if not i % n:
            return n

search = 10001

check = 3
while True:
    smallest_prime(check)
    if len(found) == search:
        print search, check
        break
    check += 2 
    

