#!/usr/bin/env  python3

"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

[[cant be copy pasted, see: https://projecteuler.net/problem=81]]

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

"""

import copy

MATRIX_IN = "p082_matrix.txt"

def parse_infile(MATRIX_IN):
    with open(MATRIX_IN) as f:
        lines = f.read().split("\n")
        for n, line in enumerate(lines):
            if line == '':
                del(lines[n])
                continue
            lines[n] = [int(i) for i in line.split(",")]
    return lines


def show(lines):
    for l in lines:
        print(l)
    print()


def first_step(lines):
    for l in range(len(lines)):
        lines[l][1] = lines[l][0] + lines[l][1]
        lines[l] = lines[l][1:]
    return lines

def step(lines):
    org = copy.deepcopy(lines)
    for y in range(len(org)):
        possible = [org[y][0]+org[y][1]]
        state = org[y][1]
        for s in range(y-1,-1,-1):
            #print("debug:", org, s)
            state += org[s][1]
            possible.append(state + org[s][0])

        state = org[y][1]
        for s in range(y+1,len(org),1):
            state += org[s][1]
            possible.append(state+org[s][0])

        lines[y][1] = min(possible)
        lines[y] = lines[y][1:]

    return lines


def load_test():
    lines = [[131, 673, 234, 103,  18],
             [201,  96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524,  37, 331]]
    return lines

def main():
    #lines = load_test()
    lines = parse_infile(MATRIX_IN)
    print("start:")
    show(lines)
    lines = first_step(lines)
    print("first:")
    show(lines)

    while len(lines[0]) > 1:
        lines = step(lines)
        show(lines)

        #return ## for now

    solution = min([ l[0] for l in lines])
    print("Solution:", solution)



if __name__ == '__main__':
    main()
