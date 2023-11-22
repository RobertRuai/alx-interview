#!/usr/bin/python3
"""determine the fewest number of coins
needed to meet a given amount
"""


def makeChange(coins, total):
    """Returns fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    tmp = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total % coin <= total:
            tmp += total // coin
            total = total % coin

    if total == 0:
        return tmp
    else:
        return -1
