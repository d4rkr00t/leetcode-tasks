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
    lo = 0
    hi = len(height) - 1
    max_left = height[lo]
    max_right = height[hi]
    ans = 0

    while lo < hi:
        cur = min(height[hi], height[lo])
        ans += max(0, min(max_left, max_right) - cur)

        if height[lo] <= height[hi]:
            lo += 1
        else:
            hi -= 1

        max_left = max(max_left, height[lo])
        max_right = max(max_right, height[hi])

    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
print(trap([4, 2, 0, 3, 2, 5]), 9)

#           5
# 4         5
# 4     3   5
# 4 2   3 2 5
# 4 2   3 2 5
# 4 2 0 3 2 5
#         l
#           h
# ml
#           mr
# ans += 4 - 2 = 0 + 2 + 4 + 1 + 2 = 9
