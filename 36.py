#!/usr/bin/env python3

palSum = 0
MAX = 1000000
for e in range(1,MAX):
    if str(e) == str(e)[::-1]: # is pal in dec
#        print(str(e),str(e)[::-1])
        if bin(e)[2:] == bin(e)[2:][::-1]: # is pal in bin
#            print(bin(e)[2:],bin(e)[2:][::-1])
            palSum += e

print(palSum)
