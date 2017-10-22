#!/usr/bin/env python3


from math import fabs
from fractions import Fraction

res = []

for x in range(10,100):
    for y in range(10,100):
        #print(y,x)
        if y == x:
            break
        if str(x)[::-1] == str(y):
            break
        if str(x)[1] == str(y)[0] or str(x)[0] == str(y)[1]:

            #print('Test case found, testing:',x,y)

            d1, d2, d3, = -1, -2, -3
            try:
                d1 = Fraction(y, x)
            except:
                pass
            try:
                d2 = Fraction(int(str(y)[0]), int(str(x)[1]))
            except:
                pass
            try:
                d3 = Fraction(int(str(y)[1]), int(str(x)[0]))
            except:
                pass
            #print('DDDD:',d1,d2,d3)



            if d1 == d2:
                print('FOUND 1-2:',d1,"==",d2, "from x,y:", x,y)
                res.append(d1)
            if d1 == d3:
                print('FOUND 1-3:',d1,d3, "from x,y:", x,y)
                res.append(d1)
            if d2 == d3:
                print('FOUND 2-3:',d2,d3, "from x,y:", x,y)
                res.append(d3)



pro = 1
for r in res:
    pro *= r

print("product of list of results:", pro )
    
