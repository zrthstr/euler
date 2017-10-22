#!/usr/bin/env python3

""" What is the value of the first triangle number to have over five hundred divisors? """

#N_DIV = 250
N_DIV = 500

def find_factors(i):
    if i == 1:
        return([1])

    f = []
    max_search = int(i ** 0.5)
    if max_search ** 2 < i:
        max_search += 1

    for p in range(1, max_search):
        if not i % p:
            f.append(p)
            other = int(i/p)
            f.append(other)

    return f

tr = 0
plus = 0
biggest = 0

while True:
    plus += 1 
    tr += plus
    fac = find_factors(tr)
    facN = len(fac)

    if facN >= N_DIV:
        print(tr,facN,fac)
        break
#    if facN > biggest:
#        biggest = facN
#    print("cur:",tr,"facN:",facN,"\t\tmaxFN",biggest)


