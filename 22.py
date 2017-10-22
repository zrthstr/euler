#!/usr/bin/env python

import re


def ord_null(n):
    if not ord("A") <=  ord(n) <= ord("Z"):
        print "unvalid char", n
        exit()

    return ord(n) - ord("A") + 1

with open("22_names.txt") as f:
    content = re.sub('"','',f.read())

names = sorted([ c for c in content.split(",") ])
print names


vals = [ sum(map(ord_null,n)) for n in names ]
print vals

total = 0
for c,v in enumerate(vals):
    print c + 1, v
    total += (c + 1) * v


print total
