# Coin Change
# https://leetcode.com/problems/coin-change/
# medium
#
# Tags: Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def coinChange(coins: [int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for c in coins:
        for i in range(1, amount + 1):
            dp[i] = min(dp[i], dp[i-c] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1


print(coinChange([1, 2, 5], 11), 3)
print(coinChange([2], 3), -1)

