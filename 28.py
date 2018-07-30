#!/usr/bin/env  python3


"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

def main():
    solution = 0

    max_height = 1001
    #max_height = 5

    diag = 1
    last = 1

    for height in range(3, max_height+1, 2):
        for side in range(4):
            last = last + height - 1
            diag += last
            #print("DEBUG: height: %d, last: %d" %(height, last))


    solution = diag
    print("Solution: %d" % solution)



if __name__ == "__main__":
    main()
