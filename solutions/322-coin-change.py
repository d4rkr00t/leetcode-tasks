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

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i - c] + 1, dp[i])

    return dp[-1] if dp[-1] < float("inf") else -1


print(coinChange([1, 2, 5], 11), 3)
print(coinChange([2], 3), -1)
print(coinChange([2, 5, 10, 1], 27), 4)

#   0 1 2 3 4 5 6 7 8 9 10 11
# 1 0
# 2 0
# 5 0
