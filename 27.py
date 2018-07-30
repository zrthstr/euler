#!/usr/bin/env  python3

"""
Euler discovered the remarkable quadratic formula:
n
2
+ n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39 .
2
However, when n = 40, 40 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly
when n
2
= 41, 41
+ 41 + 41
is clearly divisible by 41.
The incredible formula n 2 − 79n + 1601 was discovered, which produces 80 primes for the
consecutive values 0 ≤ n ≤ 79 . The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n
2
, where |a|
+ an + b
< 1000
and |b|
≤ 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and | − 4| = 4
Find the product of the coefficients, a and b , for the quadratic expression that produces the
maximum number of primes for consecutive values of n , starting with n = 0 .

"""

from eulib4 import primes_to

def main():
    max_consec_primes = 0
    maxi = 100000
    primes = primes_to(maxi)
    p_max = primes[-1]
    percent = 0.0

    for a in range(-999, 1000):
        percent += 0.1
        for b in range(-1000, 1001):
            consec = 0
            n = -1
            while True:
                n += 1
                #print("n**2 + an + b = ")
                foo = n**2 + a * n + b
                #print(foo,a,b)

                if foo > p_max:
                    raise ValueError("maxi to small..")
                if not foo in primes: 
                    break
                consec += 1 
            #print("Found consec primes: %d" % consec)

            if consec > max_consec_primes:
                print(consec, a, b, n)
                max_consec_primes = consec
                solution = a * b
                

        #print("3%f"% percent)


    print("Solution = %d" % solution)


if __name__ == '__main__':
    main()
