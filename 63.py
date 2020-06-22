#!/usr/bin/env  python3

"""
Powerful digit counts
￼  ￼  ￼
Problem 63
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

# math.log10+1 is nicer than: len(str(INT)))

import math

def main():
    for base in range(1,10):
        for ex in range(0,22):
            pro = base ** ex
            if int(math.log10(pro))+1 == ex:
                print(".")
            else:
                break



if __name__ == '__main__':
    main()
