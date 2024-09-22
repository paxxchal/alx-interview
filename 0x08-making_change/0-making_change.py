#!/usr/bin/python3
"""Module to calculate the fewest number of coins needed for a given total."""


def makeChange(coins, total):
    """Determine the fewest number of coins to meet a given amount total.

    Args:
        coins (list): List of available coin denominations.
        total (int): The amount of money to be made.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1


if __name__ == "__main__":
    # Example usage
    coins = [1, 2, 5]
    total = 11
    print(makeChange(coins, total))  # Expected output: 3 (5 + 5 + 1)
