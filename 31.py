#!/usr/bin/env python3


# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

coins = dict()
coins = {
        "1":0,
        "2":0,
        "5":0,
        "10":0,
        "20":0,
        "50":0,
        "100":0,
        "200":0
        }


t_coins = {
        "1":200,
        "2":100,
        "5":40,
        "10":20,
        "20":10,
        "50":4,
        "100":2,
        "200":1
        }

def coint_reset():
    t_coins = coins

def coin_summ(coins):
    s = 0
    for k,v in coins.items():
        s+= int(k) * v
    return 0


cs = coin_summ(coins)
print (cs)



