#!/usr/bin/env  python3

"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

... ...

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.


"""

import random
import copy

def load(filename):
    """ loads sudoku game files.
        each game consist of 10 lines.
        first line starts with Grid fllowed by
        9 * 9 numbers form 0-9
    """
    print('reading games from %s ..' % filename)

    games = []
    with open(filename) as file:
        for c, line in enumerate(file.readlines()):
            line = line.rstrip()

            if c % 10 == 0:
                games.append([])
                if not line.startswith("Grid"):
                    raise ValueError('Bad grid headder in line %d' % c)
            else:
                if not len(line) == 9:
                    raise ValueError('BAAd grid boddy in line %d' % c)
                if int(line) >= 0:
                    # throws exception if not int 
                    pass

                games[c//10].append( [{int(x)} for x in line])
 
        #if not c % 10 == 0:
        #    raise ValueError('Unfinished grid. %d lines found' % c)

    print("found %d games" % len(games))
    return games


def validate_lines(game):
    test = [[] for e in range(9)]
    if not isinstance(game, list):
        raise ValueError('Validate lines failed. "Game" type must be list is:%s. Should be list of lists' % type(game))

    for y, line in enumerate(game):
        for sq in line:
            if not isinstance(line, list):
                raise ValueError('Validation lines failed, game[x] should be list type')
            if len(sq) == 1:
                test[y].append(next(iter(sq)))

    for y, t in enumerate(test):
        if not len(t) == len(set(t)):
            raise ValueError('Two same numbers in line:', y)


def validate_sq(game):
    test = [[[],[],[]] for e in range(3)]

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            if sq == set():
                #show(game)
                raise ValueError('Some problem11, empty set found.. y: %d ,sq: %s' %(y, sq))
            if len(sq) == 1:
                test[y//3][x//3].append(next(iter((sq))))
    for te in test:
        for t in te:
            if not len(t) == len(set(t)):
                raise ValueError('Ptoblem')   


def validate_game(game):
    #print("cheking game..")
    validate_lines(game) 
    #print("lines ok..")
    validate_lines(reflect(game))
    #print("bars ok..")
    validate_sq(game)
    #print("Sqs ok..")


def reflect(game):
    """ this function reflects the sudoku field over the middle diagonale
        with this vertical and horizontal lines can be treated the same
    """
    new = [[set() for x in range(9)] for y in range(9)]

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            new[x][y] = sq

    return new


def solve_lines(game):
    for y, line in enumerate(game):
        present = set()
        for sq in line:
            if len(sq) == 1:
                present = present.union(sq)
        for x, sq in enumerate(line):
            if len(sq) > 1:
                game[y][x] = sq - present
                
    return game


def solve_fileds(game):
    present = [[set() for x in range(3) ] for y in range(3)]

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            if len(sq) == 1:
                present[y//3][x//3] = sq.union(present[y//3][x//3])

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            if not len(sq) == 1:
                game[y][x] = game[y][x] - present[y//3][x//3]

    return game


def solve_lines2(game):
    """ solves by finding single possiblitys in lines"""
    test = [[] for x in range(9)]

    for y, line in enumerate(game):
        for sq in line:
            test[y].extend(list(sq))

    found = [[] for x in range(9)]

    for y, tes in enumerate(test):
        for t in tes:
            if tes.count(t) == 1:
                found[y].append(t)

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            for f in found[y]:
                if f in game[y][x]:
                    game[y][x] = set([f])

    return game


def solve_sq2(game):
    """ see solve_line2 .. """
    test = [[[] for x in range(3)  ] for x in range(3)]    

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            test[y//3][x//3].extend(list(sq))

    found = [[[] for x in range(3)] for y in range(3)]

    for y, tes in enumerate(test):
        for x, te in enumerate(tes):
            for t in te:
                if te.count(t) == 1:
                    found[y][x].append(t)


    for y, line in enumerate(game):
        for x, sq in enumerate(game):
            for f in found[y//3][x//3]:
                if f in game[y][x]:
                    game[y][x] = set([f])
 
    return game


def count_unsolved(game):
    """ returns True if game is solved,
        returns number of possible variables needed to be ruled out,
        if game is not solved
    """
    variables = -1 * 9 * 9
    for line in game:
        for l in line:
            variables += len(l)
    return variables


def prepare(game):
    """ replaces 0 with {1..9}s .. """
    unsolved_filed = {x for x in range(1,10)}

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            if sq == {0}:
                game[y][x] = unsolved_filed.copy()

    return game


def show(game):
    #validate_lines(game)
    validate_game(game)
    print("_")
    for line in game:
        for sq in line:
            print(sq, end='')
        print()


def solve_by_logic(g):
    ## validate_game(g)
    g = solve_lines(g)
    g = reflect(solve_lines(reflect(g)))
    g = solve_fileds(g)
    g = solve_lines2(g)
    g = reflect(solve_lines2(reflect(g)))
    g = solve_sq2(g)

    return g


def mutate(game, mut):
    print("DEBUG in mutate:")
    print("DEBUG: applieing mut: %d on game:%s" %(mut, game))

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            if len(sq) == 1:
                continue
            mut -= len(sq)
            if mut < 1:
                mut *= -1

                print("DEBUG: mutating game[y][x] with mut (%s,%d)" %(game[y][x], mut))
                new = list(game[y][x])
                new.sort()
                print("DEBUG: new:", new)
                del(new[mut])
                game[y][x] = set(new)

    
                return game



def solve(game):
    c_unsolved = count_unsolved(game)
    failed_mutation = 0

    while count_unsolved(game) > 0:
        show(game)

        print("DEBUG: SWL, c_unsolved: %d , failed_mutations: %d" %(c_unsolved, failed_mutation))
        game = solve_by_logic(game)
        new_c_unsolved = count_unsolved(game)

        if c_unsolved == new_c_unsolved:
            ### if we get here we need to start guessing...
            print("DEBUG, game has not changed. Solving by brute force..")
            print("DEBUG, creating deep copy")
            gc = copy.deepcopy(game)

            failed_mutation += 1
            gc = mutate(gc,failed_mutation)

            gc = solve_by_logic(gc)
            
            try:
                validate_game(gc)
            except:
                print("DEBUG: CCCCAAAAUUGHTTTT")

            gc = solve(gc)

            #gc = random_mutate(gc)
            


        c_unsolved = new_c_unsolved

    return game


def main():
    """ games are represented as list of list of sets.
        if the fieled is know it is a set with one element
        if the field is not know yet it is either 0 or 1-9
    """

    global state

    #solution = 0
    solved_count = 0
    filename = "p096_sudoku.txt"
    games = load(filename)

    ## testing
    #del(games[0:6])
    #del(games[1:]) 

    for c, g in enumerate(games):
        print("playing game %d" % c)
        #mutations = []

        g = prepare(g)    
        g = solve(g)
        print("XXXX",g)
        print("DEBUG: done with solving: %d"% c)
        show(g)



    #print("Game solved: %d" % c)
    #print("Solution = %d" % solution)


if __name__ == '__main__':
    main()
