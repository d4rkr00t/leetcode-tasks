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

from typing import List


def maxProfit(prices: List[int]) -> int:
    lo = ans = 0

    for hi, p in enumerate(prices):
        if prices[lo] > p:
            lo = hi

        ans = max(ans, p - prices[lo])

    return ans


print(maxProfit([7, 1, 5, 3, 6, 4]), 5)
print(maxProfit([7, 6, 4, 3, 1]), 0)
