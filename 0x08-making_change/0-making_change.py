#!/usr/bin/python3
"""
Determining the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Dynamic programming approach to
    solving the problem
    """
    if total <= 0 or not isinstance(total, int):
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
