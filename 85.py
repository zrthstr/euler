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
    return sum([(xx-x)*(yy-y) for x in range(1,xx) for y in range(1,yy)])

result = dict()

MAXXY = 2000 ## calculated with rec_count()
MAXSQ = 2*1e6

def walk():
    for y in range(1,MAXXY):
        for x in range(1,MAXXY):
            if x > y:
                break
            key = str(y) + 'x' + str(x)
            count = rec_count(y, x)
            result[key] = count
            print(key, count)
            if x == 1 and count > MAXSQ:
                return
            if count > MAXSQ:
                break

def find_top():
    best_dist = MAXSQ
    best_dist_area = 0
    for k,v in result.items():
        x, y = [int(this) for this in k.split('x')]
        dist = abs(MAXSQ-v)
        if dist < best_dist:
            best_dist = dist
            best_dist_area = x * y

    print(best_dist_area)

def main():
    walk()
    find_top()

if __name__ == '__main__':
    main()

