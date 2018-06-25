#!/usr/bin/env python

"""
Problem 50 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import eulib

MAX = 10 ** 6
prime_list  = eulib.fill_prime_list(MAX)
prime_list_len = len(prime_list)

biggest_prime = 0
longest_seq = 0

def search_seq(p):
    left = 0
    right = 0
    max_seq_len = 1
    total = 2

    while True:
        if total == p:
            current_seq_len = right - left + 1
            if current_seq_len > max_seq_len:
                max_seq_len = current_seq_len
            return(p, max_seq_len)
        elif total > p:
            if right - left < max_seq_len:
                print(".")
                return(p,1) 
            total -= prime_list[left]
            left += 1
        elif total < p:
            right +=1
            total += prime_list[right]
        #print('p=%d, total=%d, left=%d, right=%d ' %(p, total, left, right), end='')
        #print('\tcurent slice = ', prime_list[left:right+1])

        if right - left < 1:
            return(p, max_seq_len)
        


if __name__ == "__main__":
    print(prime_list)
    for p in prime_list:
        prime, seq = search_seq(p)
        if seq > longest_seq:
            print("found new best result: %s with len: %d" %(prime, seq))
            longest_seq = seq
            biggest_prime = prime
        #else:
        #    print("no new best result found: %s with len: %d" %(prime, seq))
            
    
    
