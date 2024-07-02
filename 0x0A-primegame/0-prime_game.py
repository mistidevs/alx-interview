#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """
    Check if a number is a prime number
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Simulation of a game
    """
    if not isinstance(x, int):
        return 'x must be a number'
    if not isinstance(nums, list):
        return 'nums must be a list'
    maria_games_won = 0
    ben_games_won = 0
    for i in range(x):
        game_nums = [i for i in range(1, nums[i] + 1)]
        maria_score = 0
        ben_score = 0
        maria_turn = True
        while game_nums:
            prime_found = False
            for num in game_nums:
                if is_prime(num):
                    game_nums = [x for x in game_nums if x % num != 0]
                    prime_found = True
                    if maria_turn:
                        maria_score += 1
                        maria_turn = False
                    else:
                        ben_score += 1
                        maria_turn = True
                    break
            if not prime_found:
                break
        if maria_score > ben_score:
            maria_games_won += 1
        else:
            ben_games_won += 1
    if maria_games_won > ben_games_won:
        return 'Maria'
    else:
        return 'Ben'
