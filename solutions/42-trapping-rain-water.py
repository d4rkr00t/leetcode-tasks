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
    ans = 0
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(height[i], left_max[i-1])

    right_max[-1] = height[-1]
    for i in range(n-2, 0, -1):
        right_max[i] = max(height[i], right_max[i+1])

    for i in range(1, n-1):
        ans += min(left_max[i], right_max[i]) - height[i]

    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

#                      3
#          2, x  x  x  3  2  x  2
#    1, x  2, 1  x  1  3  2  1  2  1
# 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
#                      |  |
# trapped = 1
# mlo = 3
# mhi = 2
# ans = 6
