#!/usr/bin/env python

""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."""


res=[]
res.append(0)

for n in range(1,10000):
    res.append([])
    for test in range(1,n/2+1):
    #    print "test:",test, " n:", n
        if not n % test:
            res[n].append(test)


for rr in range(1,len(res)):
    new = 0
    for r in res[rr]:
        new += r
    res[rr]=new
        

print res

print len(res)

sum_all = 0

for r in range(1,len(res)):
#    print "r:%d, res[r]:%r" % (r,res[r])
    if res[r] > 10000:
        continue
    if r == res[res[r]] and r < res[r]:
        print r, res[r]
        sum_all += r + res[r]


print sum_all
