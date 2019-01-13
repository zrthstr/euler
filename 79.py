#!/usr/bin/env  python3

"""
Passcode derivation
Problem 79￼
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""


def main():
    score = {e:[] for e in range(10)}

    with open("p079_keylog.txt") as f:
        for l in f.readlines():
            l = l.strip()
            for n, c in enumerate(l, 1):
                score[int(c)].append(n)

    result = {}
    for k,v in score.items():
        if not v == []:
            result[k] = sum(v) / len(v)

    for k,v in sorted(result.items(), key=lambda kv: kv[1]):
        print(k,v)

if __name__ == '__main__':
    main()
