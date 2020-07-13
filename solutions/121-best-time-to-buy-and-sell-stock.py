# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def maxProfit(prices: [int]) -> int:
    if not prices:
        return 0

    lo = hi = 0
    profit = 0

    for i in range(len(prices)):
        n = prices[i]
        if prices[hi] < n:
            hi = i
        if prices[lo] > n:
            profit = max(profit, prices[hi] - prices[lo])
            lo = i
            hi = max(lo, hi)

    return max(profit, prices[hi] - prices[lo])


print(maxProfit([7, 1, 5, 3, 6, 4]), 5)
print(maxProfit([7, 6, 4, 3, 1]), 0)
