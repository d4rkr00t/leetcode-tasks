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
    if not prices:
        return 0

    lo = prices[0]
    ans = 0

    for hi in prices:
        if hi - lo > 0:
            ans = max(ans, hi - lo)
        else:
            lo = hi

    return ans


print(maxProfit([7, 1, 5, 3, 6, 4]), 5)
print(maxProfit([7, 6, 4, 3, 1]), 0)
