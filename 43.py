#!/usr/bin/env python3

"""
Sub-string divisibility
Problem 43￼
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


from eulib4 import primes_to

global solution
solution = 0

# dividabillity conditions
div_max = 17
cond = []
for n, p in enumerate(primes_to(div_max),1):
    cond.append({"from":n, "to":n+3, "by":p})
print(cond)

def chk_div(n):
    n = str(n)
    min_len = 10
    if len(n) < min_len:
        raise ValueError('function expects ints or stings with len >= 10. %d provided' % int(n))
    for test in cond:
        #print("testing if %s is divisable by %d" %( n[test['from']:test['to']], test['by'] ))
        if int(n[test['from']:test['to']]) % test['by']:
            return False
    return True
    
    

def mutate_all(r):
    r = list(str(r))
    global muts
    muts = []
    mutate([],r)
    return solution


def mutate(l,r):
    global solution
    for i in range(len(r)):
        left = l[:]
        if len(r) == 1:
            this = ''.join(left+[r[0]])
            if chk_div(this):
                solution += int(this)
                print("new solution %d" % solution)
            break

        right = r[:]
        this = right[i]
        right.remove(this)
        left.append(this)

        mutate(left, right)



def main():
    pandigital_sum = mutate_all(1234567890)
    #pandigital = mutate_all(1234567890)
    #pandigital = mutate_all(123455)
    print("Solution for euler 43: %d" % pandigital_sum)


if __name__ == "__main__":
    main()
