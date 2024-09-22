#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The amount to meet.

    Returns:
        int: The fewest number of coins needed to meet total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins you have, return -1.
    """
    # Handle edge case where total is 0 or less
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    # from 0 to total. Initialize all values to total + 1, which is more
    # than the maximum possible number of coins.
    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0  # 0 coins needed to make 0 amount

    # Iterate over each amount from 1 to total
    for amount in range(1, total + 1):
        # Iterate over each coin value
        for coin in coins:
            # If the coin value is less than or equal to the current amount
            if coin <= amount:
                # Update the minimum number of coins for the current amount
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    # If the minimum number of coins for the total amount is still total + 1,
    # it means the total cannot be met by any number of coins.
    if min_coins[total] == total + 1:
        return -1
    else:
        return min_coins[total]
