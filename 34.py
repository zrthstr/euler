#!/usr/bin/env python3

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''



def frac(i):
    f = 1
    for c in range(1,i+1):
        f*=c
    return f


#print(frac(1))
#print(frac(4))
#print(frac(5))


res = []

for i in range(3,1000000):
    t = 0
    for s in str(i):
        t+=frac(int(s))
    if t == i:
        print(t, i)
        res.append(t)

print(res)
su = 0
for r in res:
    su +=r
print("result:", su)


