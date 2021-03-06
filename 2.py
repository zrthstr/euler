#!/usr/bin/env python

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
		1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fib():
	a, b = 1, 2
	while True:
		yield a
		aa = a
		a = b
		b = b + aa

MAX = 4 * 10**6
print MAX
s = 0

for f in fib():
	if f > MAX:
		print "max reached, exiting!"
		break
	if not f % 2:
		s+=f
	print f

print "summ:", s



