
first = 1
sec = 2

maxi = 4 * 10 ** 6

ev_sum = 0

while sec <= maxi:
    print first, sec, ev_sum 
    tmp = first
    first = sec
    sec += tmp

    if not first % 2:
        if first <= maxi:
            ev_sum += first
            print "new_vaule: ", ev_sum
