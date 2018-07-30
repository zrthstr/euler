#!/usr/bin/env  python3

"""
Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:
0.12345678910 1 112131415161718192021...
It can be seen that the 12 th digit of the fractional part is 1.
If d n represents the n th digit of the fractional part, find the value of the following expression.
d 1 × d 10 × d 100 × d 1000 × d 10000 × d 100000 × d 1000000

"""


def main():
    solution = 1
    #d = "0."
    d = "."
    s = 0

    needed_len = 10 ** 7
    #needed_len = 100

    while len(d) < needed_len:
        s += 1
        d += str(s)
    
     
    for e in range(0,8):
        print("d[%d] = %s" %(10**e  ,d[10**e]))
        solution *= int(d[10**e])

    print("Solution = %d" % solution)


if __name__ == '__main__':
    main()
