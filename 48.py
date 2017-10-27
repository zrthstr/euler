#!/usr/bin/env python2

"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000** 1000.
"""

euler48 = str(sum(e**e for e in range(1,1001)))[-10:]
print euler48
