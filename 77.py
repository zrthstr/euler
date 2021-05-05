#!/usr/bin/env python3

"""
Problem 77: Prime summations


It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

"""


# dividing 100 into two positive integers is the same as 99 into any amount of positive ints

def change(n, p):
    if n == 0:
        return 1
    elif n < 0 or p == []:
        return 0

    return change(n, p[:-1]) + change(n - p[-1], p)

import eulib

if __name__ == "__main__":
    start = 5
    while True:
        start += 1
        n_combs = change(start, eulib.fill_prime_list(start))
        if n_combs > 5000:
            break
        else:
            print("nope: ", n_combs)
    print("Found: ", start, n_combs)
