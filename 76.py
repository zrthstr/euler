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

def test():
    ## solve for 5 ##
    v4 = 4
    for n4 in range(0, 2):
        v3 = 3
        for n3 in range(0, 2):
            v2 = 2
            for n2 in range(0, 3):
                v1 = 1
                for n1 in range(0,6):
                    if v4 * n4 + v3 * n3 + n2 * v2 + v1 * n1 == 5:
                        print(f"v4:{n4} v3:{n3} v2:{n2} v1:{v1}")


def calc(n, load):
    if n == 0:
        return load
    print(n)
    #for n in range(0, n+1):
    load = calc(n-1)
    if load == 100:
        print(".")

def main():
    #test()
    calc(99,0)



if __name__ == '__main__':
    main()
