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
    low = high = ans = 0

    for i in range(len(prices)):
        ans = max(ans, prices[high] - prices[low])

        if prices[i] < prices[low]:
            low = i
            high = max(i, high)

        if prices[i] > prices[high]:
            high = i

    return max(ans, prices[high] - prices[low])


print(maxProfit([7,1,5,3,6,4]), 5)
print(maxProfit([7,6,4,3,1]), 0)
