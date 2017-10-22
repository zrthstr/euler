#!/usr/bin/env python3



MAX = 999999
primes = [2,3]

def fill_prime_list(maximum):
    for i in range(5, maximum + 1, 2):
        for c in primes: 
            if i % c  == 0: ## not prime or allready there
                break
        else:
            primes.append(i)
#            return True



def circ(i):
    all_c = []
    i = str(i)
    org_i = i
    while True:
        i = i[1:] + i[:1]
        if i in all_c:
            return all_c
        all_c.append(i)


    

fill_prime_list(MAX)


print(primes)
print(len(primes))


res = []

for p in primes:
#    for e in ["2","4","5","6","8","0"]:
#        if e in str(p):
#            break

    cc = circ(p)
    for c in cc:
        if not int(c) in primes:
            break
    else:
        res.append(cc)

        #cc.sort()
        #if cc not in res:
        #    res.append(cc)


for r in res:
    print(r)

print(len(res))

            










