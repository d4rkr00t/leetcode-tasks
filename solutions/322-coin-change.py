# Coin Change
# https://leetcode.com/problems/coin-change/
# medium
#
# Tags: Amazon, Microsoft, Google
#
# Time:  O(n*c)
# Space: O(n)
#
# Solution:
# TBD

def coinChange(coins: [int], amount: int) -> int:
    dp = [float("inf")] * (amount+1)
    dp[0] = 0

    for c in coins:
        for i in range(c, amount + 1):
            dp[i] = min(dp[i], dp[i-c] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1

print(coinChange([1, 2, 5], 11), 3)
print(coinChange([2], 3), -1)
print(coinChange([2,5,10,1], 27), 4)
print(coinChange([186,419,83,408], 6249), 20)

#   0 1 2 3 4 5 6 7 8 9 10 11
# 1 0
# 2 0 1 1 2 2 3 3 4 4 5 5  6
# 5 0 1 1 2 2 1 2 2 3 3 2  3

#   0 1 2 3
# 2 0 0 1 0
#
#
