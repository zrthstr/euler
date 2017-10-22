#!/usr/bin/python

import math

#test = [0,1]
test = [0,1,2,3,4,5,6,7,8,9]
#test = [0,1,2,3]

"""
0 1 2 3
0 1 3 2
0 2 1 3
0 2 3 1
0 3 1 2
0 3 2 1

1 0 2 3
1 0 3 2...
"""

muts = []

global i
i = 0

def mut(pre, rest):
    if len(rest) == 1:
        #print "new:", i, pre + rest
        this = "".join([str(x) for x in pre + rest])
        #print this
        muts.append(this)
    for e in rest:
        copy = rest[:]
        copy.remove(e)
        mut(pre + [e], copy) 


mut([],test)

print muts[999999]


#for e in range(math.factorial(len(l))):
#    print e,">", l
