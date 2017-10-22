#!/usr/bin/env python

from sets import Set
res=[]

upper = 28123
#upper /= 1000

for n in range(1,upper):
    res.append([ test for test in range(1,n/2+1) if not n % test ])


#res =    [[ test for test in range(1,n/2+1) if not n % test ] for n in range(1,upper)]


print res

#exit() 

# ab = [c for c,v in enumerate(res) if c < sum(v) ]

ab = [c+1 for c,v in enumerate(res) if c+1 < sum(v) ]

print ab

sums = Set() 
for a in ab:
    for b in ab:
        if a+b < 28124:
            sums.add(a+b)

sss = 0
for e in range(len(sums)):
    if e not in sums:
        print e
        sss+=e

 

print len(sums)

print sss
