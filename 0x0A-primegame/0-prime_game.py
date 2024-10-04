#!/usr/bin/python3
"""
Module: 0-prime_game
Defines the isWinner function to determine the winner of the Prime Game.
"""


def isWinner(x, nums):
    """
    Determines the player who won the most rounds of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the value of n for each round.

    Returns:
        str: The name of the player that won the most rounds ("Maria" or "Ben").
             Returns None if there is no clear winner.
    """
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(limit):
        """
        Generates a list indicating the primality of numbers up to limit.

        Args:
            limit (int): The upper bound of numbers to check for primality.

        Returns:
            list: A boolean list where index represents the number and the value
                  at that index is True if the number is prime, else False.
        """
        sieve = [False, False] + [True] * (limit - 1)
        for num in range(2, int(limit ** 0.5) + 1):
            if sieve[num]:
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False
        return sieve

    max_n = max(nums)
    sieve = sieve_of_eratosthenes(max_n)
    prime_counts = [0] * (max_n + 1)
    count = 0

    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue
        primes = prime_counts[n]
        if primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
