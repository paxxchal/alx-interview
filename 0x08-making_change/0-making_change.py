#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the array for storing the minimum coins needed for each amount
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1


if __name__ == "__main__":
    coins = [1, 2, 5]  # Example coin denominations
    total = 11  # Example total amount
    print(makeChange(coins, total))  # Output should be 3 (5 + 5 + 1)
