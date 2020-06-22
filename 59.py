#!/usr/bin/env  python3

"""
XOR decryption
￼  ￼  ￼
Problem 59

"""
import string

INFILE = 'p059_cipher.txt'

prob = dict({" ":1200, "e":1100, "t":935, "a":850, "r":758, "i":754})

def readfile(infile):
    with open(infile) as f:
        lines = [int(i) for i in f.read().split(",")]
        #print(type(lines[0]))
    return lines

# english score
def escore(randb, key):
    alpnum = string.ascii_lowercase + string.digits
    score = 0
    for b in randb:
        b = chr(b ^ key)
        if b in prob:
            score += prob[b]
        elif b in alpnum:
            score += 150
        else:
            score += 1
    return score


def main():
    bytes_in = readfile(INFILE)
    for b in bytes_in:
        print(chr(b),end='')
    print()

    # split encrypted text in three slices
    l0, l1, l2 = list(), list(), list()
    for i in range(0,len(bytes_in)-2,3):
        l0.append(bytes_in[i])
        l1.append(bytes_in[i+1])
        l2.append(bytes_in[i+2])

    # find top score key for each slice
    key = list()
    for this in [l0, l1, l2]:
        max_score = 0
        max_key = 0
        for testkey in range(128):
            score = escore(this, testkey)
            if score > max_score:
                max_score = score
                max_key = testkey
        print("result:",max_score, chr(max_key))
        key.append(max_key)


    answer = 0
    for n, b in enumerate(bytes_in):
        k = key[n%3]
        print(chr(k ^ b), end='')
        answer += k ^ b
    print()
    print("answer:",answer)



if __name__ == '__main__':
    main()
