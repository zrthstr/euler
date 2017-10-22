
import math

q = 600851475143
start = 2
# maxi = int(math.sqrt(q))


def first_prime(num,start):
    while start <= num:
        if num % start == 0:
            return start
        start+=1

aa = q
while True:
    q = first_prime(aa,2)
    print q
    if aa == q:
        break
    aa/=q

