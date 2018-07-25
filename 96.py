#!/usr/bin/env  python3

"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

... ...

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.


"""


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

    for y, line in enumerate(game):
        for sq in line:
            if sq == set():
                raise ValueError('Some problem00, empty set found.. y: %d, sq: %s' %(y, sq))
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


state = 0

def has_changed(game):
    global state
    leng = 0
    for line in game:
        for l in line:
            leng += len(l)
    if state == leng:
        return False
    else:
        state = leng
        return True



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



def is_solved(game):
    for line in game:
        for l in line:
            if len(l) > 1:
                return False
    return True


def prepare(game):
    """ replaces 0 with {1..9}s .. """
    unsolved_filed = {x for x in range(1,10)}

    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            if sq == {0}:
                game[y][x] = unsolved_filed.copy()

    return game


def show(game):
    print("_")
    for line in game:
        for sq in line:
            print(sq, end='')
        print()


def solve_by_logic(g):
    validate_game(g)
    g = solve_lines(g)
    g = reflect(solve_lines(reflect(g)))
    g = solve_fileds(g)
    g = solve_lines2(g)
    g = reflect(solve_lines2(reflect(g)))
    g = solve_sq2(g)

    return g


def mutate(game, x):
    print("DEBUG mutating: ", x)
    for y, line in enumerate(game):
        for x, sq in enumerate(line):
            if len(sq) > 1:
                x -= 1
                if x == 0:
                    game[y][x].pop()
                    return game

    #return game

def main():
    """ games are represented as list of list of sets.
        if the fieled is know it is a set with one element
        if the field is not know yet it is either 0 or 1-9
    """

    solution = 0
    solved_count = 0
    filename = "p096_sudoku.txt"
    games = load(filename)

    ## testing
    del(games[0:6])
    del(games[1:]) 

    for c, g in enumerate(games):
        print("playing game %d" % c)
        rounds = 0
        g = prepare(g)    
        mutations = []

        while not is_solved(g):
            rounds += 1
            g = solve_by_logic(g)

            if not has_changed(g):
                ### we give up for now.. next.
                #solved_count -= 1
                
                
                break



        #print("Rounds played: %d" % rounds)
        solved_count += 1
        print("Games solved: %d" % solved_count)
 
    print("Solution = %d" % solution)


if __name__ == '__main__':
    main()
