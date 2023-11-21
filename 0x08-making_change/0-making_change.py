#!/usr/bin/python3
"""determine the fewest number of coins
needed to meet a given amount
"""
import sys


def makeChange(coins, total):
    """Returns fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    res = sys.maxsize

    for i in range(len(coins)):
        if (coins[i] <= total):
            sub_res = makeChange(coins, total-coins[i])

            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    if res == -sys.maxsize:
        return -1
    else:
        return res
