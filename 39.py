#!/usr/bin/env  python3

"""
Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly
three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?

"""

import math

def pyth_count(t):
    
    ### a**2 + b ** 2 == c ** 2
    ### a + b + c == t
    pass


def main():
    solutions = [0 for x in range(1001)]
    
    for a in range(1,1000):
        for b in range(1,1000):
            cc = a**2 + b**2
            c = math.sqrt(cc)
            if not c.is_integer():
                continue
            s = a + b + c
            if s > 1000:
                break
            print("XX ",s, a,b,c)
            solutions[int(s)] += 1 


    print("Solution: %d" % solutions.index(max(solutions)))

if __name__ == '__main__':
    main()
