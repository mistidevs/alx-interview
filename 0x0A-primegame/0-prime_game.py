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
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'


"""
def isWinner(x, nums):
    if not isinstance(x, int):
        return 'x must be a number'
    if not isinstance(nums, list):
        return 'nums must be a list'
    if x <= 0:
        return None
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
"""
