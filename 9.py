#!/usr/bin/env python

"""
Find the greatest product of five consecutive digits in the 1000-digit number.
"""

import math


for a in range(1,1000):
    for b in range(1,1000):
        c = math.sqrt(a ** 2 + b ** 2)
        if c %1:
            continue
        if a < b < c:
            abc = int(a + b + c)

            print "found: a:%d b:%d c%d ===> " , (a,b,c,abc) 
            if abc == 1000:
                print "Found: %d", a * b * c 
