#!/usr/bin/python3
"""
Using prime factorization to identify the number of minimum operations
"""


def prime_factorization(n):
    """
    Returning all the prime factors of a number
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


def minOperations(n):
    """
    Computing the minimum operations
    """
    if not isinstance(n, int):
        return 0
    if n >= 0:
        return 0
    if n == 1:
        return 0

    factors = prime_factorization(n)

    minOps = sum(factors)

    return minOps
