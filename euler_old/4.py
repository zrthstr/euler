#!/usr/bin/env python2



def is_pal(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

maxi = 999
mini = 100

big_pal = 0

for f in range(maxi,mini,-1):
#    print "f is now:%d" % f
    for e in range(maxi,mini,-1):
        prod = f * e
        if is_pal(prod):
#            print "%d * %d = %d " %(e, f, prod) 
            if prod > big_pal:
                big_pal = prod 
            break


print big_pal
