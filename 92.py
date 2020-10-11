#!/usr/bin/env  python3

"""
Square digit chains
￼  ￼  ￼
Problem 92
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

to1 = set([1])
to89 = set([89])

def sortdigits(n):
    return int("".join(sorted(str(n))))

def sqadd(n):
    s = 0
    for d in str(n):
        s += int(d)**2
    return s

def reduce(n):
    n = sortdigits(n)
    sofar = set([n])
    while True:

        if n in to1:
            to1.update(sofar)
            return 1
        elif n in to89:
            to89.update(sofar)
            return 89

        n = sqadd(n)
        n = sortdigits(n)
        sofar.add(n)


def main():
    count1 = 0
    count89 = 0

    #for n in range(1,int(10e5)):
    for n in range(1,int(10e6)):  # 10M
    #for n in range(1,int(10e4)):
        print("processing:",n)
        ret = reduce(n)
        if ret == 1:
            count1 += 1
        if ret == 89:
            count89 += 1

    print("")
    print("count1",count1)
    print("count89",count89)
    print("len(to1)", len(to1))
    print("len(to89)", len(to89))

if __name__ == '__main__':
    main()
