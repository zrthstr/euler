#!/usr/bin/env python


def route(n):
    pos = 1
    for x in range(2*n,n,-1):
        pos *= x 


    sub = 1
    for x in range(n,0,-1):
        sub *= x

    return pos / sub
    


print route(20)

