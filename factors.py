#!/usr/bin/env python3

import math
from collections import Counter


def prime_gen():
    cur = 3
    p = [2]
    yield p[0]

    while True:
        for test in range(3,int(math.sqrt(p[-1]))+1):
            if cur % test == 0:
                break
        else:
            p.append(cur)
            yield p[-1]
    
        cur += 2


def primes_to(maxi):
    if maxi <= 2:
        return []
    if maxi == 2:
        return [2]

    p = [2]
    for n in range(3,maxi+1, 2):
        for test in range(3,int(math.sqrt(n))+1):
            if n % test == 0:
                break
        else:
            p.append(n)
    return p


def primes_count(n):
        return [prime_iterator() for p in range(n)]
            

def factors(i):
    if i < 2:
        return []

    factors = []
    primes = primes_to(i)

    if i in primes:
        return [i]
    
    while i not in primes:
        for test in primes: #sqrt(i)
            if i % test == 0: 
                i //= test
                factors.append(test)
                break
    factors.append(i)
    return factors


def uniq_factors(i):
    return list(set(factors(i)))


def count_factors(i):
    return dict(Counter(factors(i)))



def main():

    #a = primes_under(100000)
    #print(a)
    #a = [prime_gen() for p in range(100)]
    #for a in prime_gen():
    #    print(a)
    #a = factors(16)
    print(a)

    #for i in [0,1,2,10,13,100,101,19991]:
    #    print(i, "->", factors(i))
    #    print(i, "->", count_factors(i))
    #    print(i, "->", uniq_factors(i))


if __name__ == '__main__':
    main()
