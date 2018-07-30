#!/usr/bin/env  python3

"""
Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""


def main():
    solution = 0

    x = 100
    while True:
        x+=1

        xl = list(str(x))
        xl.sort()
        for t in range(2,7):
            tmp = t * x
            tmp = list(str(tmp))
            tmp.sort()
            if not tmp == xl:
                break
        else:
            print("Solution = %d" % x)
            return


if __name__ == '__main__':
    main()
