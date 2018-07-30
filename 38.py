#!/usr/bin/env  python3

"""
Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the
concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product
of an integer with (1,2, ... , n ) where n > 1?

"""

def is_9_pd(n):
    n = str(n)
    for t in range(1,10):
        if not str(t) in n:
            return False
    return True


def main():
    solution = 0
    
    for c in range(9876 + 1):
        #a = str(c) + str(c*2)
        #if "0" in a:
        #    continue
        test = ""
        for n in range(1, 10):
            test += str( n * c )
            if len(test) == 9:
                if is_9_pd(test):
                    print("test",test, c, n)

    print("Solution = %d" % solution)


if __name__ == '__main__':
    main()
