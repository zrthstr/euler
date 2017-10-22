#!/usr/bin/env  python3

import eulib


count = 0
i = 0

primes = eulib.fill_prime_list(800000)
print("primes prepared")



def is_rt(p):
    if p > 10:
        p = p // 10
        if not p in primes:
            return False
        else:
            return is_rt(p)
    return True


def is_lt(p):
    if p > 10:
        p = int(str(p)[1:])
        if not p in primes:
            return False
        else:
            return is_lt(p)
    return True


found = []
for p in primes:
    if is_rt(p):
        if is_lt(p):
            if p > 9:
                found.append(p)




fsum = sum(found)
print("found:",found,)
print("count(found)",len(found))
print("sum(found)",fsum)


