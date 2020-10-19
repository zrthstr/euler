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

"""
6
5 + 1
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1
"""

"""
7
6 + 1
5 + 2
4 + 3
4 + 2 + 1
4 + 1 + 1 + 1
3 + 3 + 1
3 + 2 + 2 + 1
3 + 2 + 1 + 1 + 1
3 + 1 + 1 + 1 + 1 + 1
2 + 2 + 2 + 2 + 1
2 + 2 + 2 + 1 + 1 + 1
2 + 2 + 1 + 1 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
etc
"""


def mutate(this):
    print()
    print(f"got {this}")
    for i, n in enumerate(this):
        #if n:
        if n == 1:
            continue
        print(f"looking at {this[i]} ") ## {n}")

        this[i] = this[i]-1

        rest = start - sum(this[i:])
        #rest = start
        t, r = divmod(rest, this[i])
        if r == 0:
            add = [rest] * t
        else:
            add = [rest] * t + [r]

        print(f"t:{t}, r:{r}, this[i]:{this[i]}, rest:{rest} add:{add}")
        return add + this[i:]




def main():
    """ for simplicity reason lets run this form right to left,
        flipped compared to above"""

    global start
    start = 6
    start = 5
    this = [start]

    print(this)
    while not set(this) == {1}:
        this = mutate(this)
        print(this)


if __name__ == '__main__':
    main()
