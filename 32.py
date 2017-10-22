#!/usr/bin/env python3


def han(cc): # has all numbers?
    cc = str(cc)
    index = [0,0,0,0,0,0,0,0,0,0]

    for c in cc:
        index[int(c)]+=1
    if index == [0,1,1,1,1,1,1,1,1,1]:
        return True
    else:
        return False


known = []
pro = 0

def store(cc):
    if cc in known:
        return
    else:
        global pro
        pro += cc
        known.append(cc)



tmax = 9876
xmax = 222
ymax = 2222


for x in range(1,10800):
    for y in range(1,10800):
        if y > x:
            break
    #    if x * y > MAX:
    #        print("too big:", MAX)
    #        continue
        
        a = han(str(x) + str (y) + str(x*y))
        if a:
            #if x < y:
            #    tmp = x
            #    x = y
            #    y = x

            store(x*y)
            print(a,': x',x,'z',y,"xz",x*y,"sum", pro)
            break
        

r = han(140000100)
print(r)

print(known)
print('pro:',pro)
