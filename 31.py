#!/usr/bin/env python3

### see 76 for a clean solution ###

"""
calculate the combinationbs that 200p can be combined with
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

"""
 

### a quite ugly but sill ok fast solution..
def main():
    count = 0
    for p1 in range(0,201):
        for p2 in range(0, 101):
            if p1 + p2 * 2:
                break
            for p5 in range(0, 41):
                if p1 + p2 * 2 + p5 * 5 > 200:
                    break
                for p10 in range(0, 21):
                    if p1 + p2 * 2 + p5 * 5 + p10 * 10 > 200:
                        break
                    for p20 in range(0, 11):
                        for p50 in range(0, 5):
                            for p100 in range(0, 3):
                                for p200 in range(0, 2): 
                                    cs = p1 + p2 *2 + p5 * 5 + p10 * 10 + p20 * 20 + p50 * 50 + p100 * 100 + p200 * 200
                                    if cs == 200:
                                        count += 1
    print(count)

if __name__ == "__main__":
    main()

