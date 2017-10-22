
import math

q = 600851475143

def first_prime(num,start):
    while start <= num:
        if num % start == 0:
            return start
        start+=1

aa = q
p = 2
while True:
    p = first_prime(aa,p)
    print p
    if aa == p:
        break
    aa/=p

