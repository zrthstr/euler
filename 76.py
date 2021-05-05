#!/usr/bin/env  python3

"""
Counting summations - Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

"""

''' http://www.luschny.de/math/seq/PartitionsOf9.htm '''

# dividing 100 into two positive integers is the same as 99 into any amount of positive ints

def change(n, p):
    if n == 0:
        return 1
    elif n < 0 or p == []:
        return 0

    return change(n, p[:-1]) + change(n - p[-1], p)


if __name__ == "__main__":
    print(change(100, list(range(1,100))))
