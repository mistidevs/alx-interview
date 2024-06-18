#!/usr/bin/python3
"""
Determining the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Using sorting and iteration to solve
    the problem
    """
    if total <= 0 or not isinstance(total, int):
        return 0

    if len(coins) == 0:
        return 0

    num_coins = 0
    i = 0
    coins.sort(reverse=True)

    while i < len(coins):
        if total >= coins[i]:
            total = total - coins[i]
            num_coins += 1
        elif total == 0:
            return num_coins
        elif i == (len(coins) - 1):
            return -1
        elif total < coins[i]:
            i += 1
            continue
