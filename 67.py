#!/usr/bin/env  python3

"""
Maximum path sum II
Problem 67￼
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

"""




def main():


    with open("p067_triangle.txt") as f:
        raw = f.read()

    pyr = [[ int(e) for e in line.split()] for line in raw.split('\n') if not line == ""]
    print(pyr)


    for ln in reversed(range(len(pyr)-1)):
        for x in range(len(pyr[ln])):
            print("..", ln, x)
            pyr[ln][x] = pyr[ln][x] + max(pyr[ln + 1][x], pyr[ln + 1][x+1])

    print("Solution = %d" % pyr[0][0])


if __name__ == '__main__':
    main()
