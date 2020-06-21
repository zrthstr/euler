#!/usr/bin/env  python3

"""
Problem 85 - Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

[https://projecteuler.net/problem=85]
[https://projecteuler.net/project/images/p085.png]


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""

def rec_count(xx,yy):
    xx += 1
    yy += 1
    a = 0
    for x in range(1,xx+1):
        for y in range(1, yy+1):
            a+=(xx+1-x) * (yy+1-y)
            print(a)
    return a

result = dict()

MAXXY = 3 ## something below 1m ...
MAXSQ = 1000 # should be 2M

def interate():
    for y in range(MAXXY,1):
        for x in range(MAXXY,1):
            if x > y:
                x, y = y, x
            key = str(y) + 'x' + str(x)
            if not key in result:
                count = rec_count(y, x)
                result[key] = count
            if count > 20000000:
                break
                if x == 1:
                    return

def main():
    #iterate()
    #find_top()
    test = rec_count(2,3)
    print(test)


if __name__ == '__main__':
    main()

