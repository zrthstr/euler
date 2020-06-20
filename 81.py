#!/usr/bin/env  python3

"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

[[cant be copy pasted, see: https://projecteuler.net/problem=81]]

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

"""

MATRIX_IN = "p081_matrix.txt"

def calulate_number_of_path(n):
    pos = 1
    for x in range(2*n,n,-1):
        pos *= x
    sub = 1
    for x in range(n,0,-1):
        sub *= x
    return pos / sub

def flip(lines):
    # flip by 45 deg
    #
    # from [[0 1 2]
    #       [3 4 5]
    #       [6 7 8]]
    #
    # to   [    [0]
    #         [3] [1]
    #       [6] [4] [2]
    #         [7] [5]
    #           [8]    ]

    out = [[] for i in range(2*len(lines)-1)]
    for n, line in enumerate(lines):
        for ln, l in enumerate(line):
            out[n+ln].insert(0,l)
    return out

LATTIC = list()

def test_flip():
    #test_lines = [[0,1,2],[3,4,5],[6,7,8]]
    lines = [[131, 673, 234, 103,  18],
             [201,  96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524,  37, 331]]
    flipped = flip(lines)
    print("in:", lines)
    print("flipped:", flip(lines))
    pprint(flipped)


def parse_infile(MATRIX_IN):
    with open(MATRIX_IN) as f:
        lines = f.read().split("\n")
        for n, line in enumerate(lines):
            if line == '':
                del(lines[n])
                continue
            lines[n] = [int(i) for i in line.split(",")]
    return lines

def pprint(lines):
    width = int(len(lines) /2)
    for n, line in enumerate(lines, - int(width)):
        print("   " * abs(n), line)


def main():
    #print("a North-East grid at 80x80 has %d paths" % calulate_number_of_path(80))
    test_flip()
    #lines = parse_infile(MATRIX_IN)
    #print(lines)
    #lines = flip(lines)
    #print(lines)
    #pprint(lines)
    #min_path(lines)


if __name__ == '__main__':
    main()
