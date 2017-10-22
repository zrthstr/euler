


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False   # NO PRIME
    return True # PRIME


def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return i   # NO PRIME
    return n # PRIME



primes = []
maxi = 20

test = 64

###  works
while 1:
#    print test
    print prime(test)
    test = test / prime(test)
    if test == 1:
        break

#print primes
#print sorted(set(primes))
