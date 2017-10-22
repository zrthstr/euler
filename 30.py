#!/usr/bin/env python2


"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


SQ = 5
# FROM = 1 * 10 ** (LEN -1 )  
#TO = (1 * 10 ** LEN) - 1 

# print "LEN, TO :", LEN, TO



found = []

for i in xrange(2, 400000):

    i_str = str(i)

    summ = 0
    for digit in i_str:
        summ += int(digit) ** SQ


    if summ == i:
        found.append(summ)
        print "winner:", summ


print "Found:" , found
print "sum_sum", sum(found) 
