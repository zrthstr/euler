



size = 1001
size = 11
field = [[ 0 for f in range(size) ]  for e in range(size) ]


def spirol(size):

    # [x,y]
    di = {"right":[1,0],"left":[-1,0],"up":[0,1],"down":[0,-1]}
    mid = (size -1)/2
    pos = [mid, mid]


    adder = di["right"]

    gc = 2
    tc = 1

    for c in range(size ** 2):
        print "adder:",adder
        print "gc:",gc,"tc:", tc, 

        pos = [pos[0] + adder[0], pos[1] + adder[1]]

        print "pos1,2:",pos[0], pos[1]

        tc -= 1
        if adder == di["down"] and tc == 0:
            gc += 1

 

        if tc == 0:
            if adder == di["right"]:
                adder = di["down"]
            elif adder == di["down"]:
                adder = di["left"]
            elif adder == di["left"]:
                adder = di["up"]
            else:
                adder = di["right"]
   
        tc = gc

        yield [x,y]





mid = (size -1 )/ 2

s = [mid,mid]


for x,y in spirol(size):
#    field[s[0]][s[1]] = c 
    print x,y


for f in field:
    print f                


