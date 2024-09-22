#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list of int): The values of the coins in your possession.
    total (int): The total amount to make change for.

    Returns:
    int: Fewest number of coins needed to meet total.
         Returns 0 if total is 0 or less.
         Returns -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    min_coins = [float("inf")] * (total + 1)
    min_coins[0] = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # Update min_coins[i] if using this coin results in fewer coins
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # If min_coins[total] is still infinity, it means we couldn't make the total
    return min_coins[total] if min_coins[total] != float("inf") else -1
