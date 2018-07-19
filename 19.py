#!/usr/bin/env  python3

"""
Counting Sundays
Problem 19 
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


### the smart solution is to do print(1200/7) ## ==>> 171 ...

"""


def is_leap(year):
    return year % 4 is 0 and (year % 100 is not 0 or year % 400 is 0)


def build_year():
    global l_year, nl_year, l_count, nl_count, l_first, nl_first
    
    jan, feb_l, feb_nl, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = \
    31,  29,    28,     31,  30,  31,  30,  31,  31,  30,  31,  30,  31

    nl_year = [jan, feb_nl, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    l_year = nl_year[:]
    l_year[1] = feb_l

    l_count = sum(l_year)
    nl_count = sum(nl_year)

    l_first = [1]
    for month in l_year[:-1]:
        l_first.append(l_first[-1]+month)

    nl_first = [1]
    for month in nl_year[:-1]:
        nl_first.append(nl_first[-1]+month)


def build_week():
    # sunnday --> 0
    # saturday --> 6
    global day_of_week, so, mo, tu, we, th, fr, sa
    so, mo, tu, we, th, fr, sa = 0, 1, 2, 3, 4, 5, 6
    day_of_week = ['So', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


def show_year():
    print("l_year:\t\t", l_year)
    print("nl_year:\t", nl_year)

    print("l_first:\t",l_first)
    print("nl_first:\t",nl_first)

    print("l_count:\t",l_count)
    print("nl_count:\t",nl_count)

    #print("First of 1901 is a _%s_day." % day_of_week[first_weekday_1901()])


def count_first_sunndays(year, weekday_jan_first):
    first_sun_count = 0
    if is_leap(year):
        this_year = l_first
    else:
        this_year = nl_first 

    for day in this_year:
        day += weekday_jan_first
        if day % 7 == 0:
            first_sun_count += 1
            #print("Found another fist sunnday:", first_sun_count)

    return first_sun_count


def first_weekday(year, last_started_with):
    
    if is_leap(year - 1):
        len_year = l_count
    else:
        len_year = nl_count

    return (len_year + last_started_with) % 7


def main():
    build_year()
    build_week()
    show_year()

    start_y = 1901
    end_y = 2000
    solution = 0
    first_last_year = 1

    for year in range(start_y, end_y+1):
        first = first_weekday(year, first_last_year)        
        first_sunndays = count_first_sunndays(year, first)
        
        print("year %d is leap year: %d and starts with %s and has %d first_sunndays" % (year, is_leap(year), day_of_week[first], first_sunndays))
        solution += first_sunndays
        first_last_year = first

        

    print("Solution = %d" % solution)

if __name__ == '__main__':
    main()
