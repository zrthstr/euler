#!/usr/bin/env  python3

"""
Spiral primes - Problem 58
￼  ￼  ￼
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

"""

import sys
import eulib4


ppool = set(eulib4.primes_to(4000000))


def main():
    print(".")
    spiral = 1
    is_prime = 0
    corners = 1

    print(spiral)
    for e in range(2,sys.maxsize,2):
        for f in range(4):
            corners += 1
            spiral += e
            if spiral in ppool:
                is_prime += 1
                #print("prime: ", spiral)

        slen = e + 1
        ratio = is_prime / corners
        print(f"corners: {corners}, is_prime: {is_prime}, ratio {ratio}, spiral: {spiral} slen: {slen}")
        if ratio < 0.1:
            print(f"solution: {slen}")
            break

if __name__ == '__main__':
    main()
