#!/usr/bin/python3
"""
Module to find the minimum number of operations
to achieve exactly n H characters in a file
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
    n (int): The target number of H characters

    Returns:
    int: The minimum number of operations needed
    to achieve n H characters, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
