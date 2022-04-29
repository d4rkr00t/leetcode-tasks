# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# hard
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    lr = [0] * n
    prev = ans = 0
    for i, h in enumerate(height):
        prev = max(prev, h)
        lr[i] = prev

    prev = 0
    for i in range(n - 1, -1, -1):
        cur = height[i]
        tmp = min(prev, lr[i]) - cur
        if tmp > 0:
            ans += tmp
        prev = max(cur, prev)

    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
