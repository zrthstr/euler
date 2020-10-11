#!/usr/bin/env  python3

"""
Reciprocal cycles
Problem 26￼
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""


def rec_cycle_len(e):
    seen = set()
    last = 1
    result = "0."
    while True:
        last *= 10
        if last < e:
            result += "0"
            continue

        q, last = divmod(last, e)
        result += str(q)

        if last in seen:
            break
        seen.add(last)
        if last == 0:
            break

    return [len(seen), result]


def main():
    print(max(rec_cycle_len(e) for e in range(2,1000))[0])


if __name__ == '__main__':
    main()
