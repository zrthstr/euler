#!/usr/bin/env python2


def fill_prime_list(maximum):
    primes = [2,3,5,7]
    for e in range(11, maximum + 1, 2):
        if not (e % 3) * (e % 5) * (e % 7):
            continue
        if e in primes:
            continue
        for c in range(2,e//2+1): 
            if e % c  == 0: ## not prime or allready there
                break
        else:
            primes.append(e)
    return primes


if __name__ == "__main__":
    import sys
    print fill_prime_list(int(sys.argv[1]))
