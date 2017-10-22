#!/usr/bin/env python

"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

maximum = 100
maximum += 1

su_sq = reduce(lambda x, y: x + y, range(1,maximum)) ** 2
sq_su = sum(x**2 for x in range(1,maximum)) 


print su_sq - sq_su



