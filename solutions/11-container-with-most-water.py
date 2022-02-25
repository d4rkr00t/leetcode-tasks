# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# medium
#
# Tags: Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def maxArea(height: List[int]) -> int:
    ans = 0
    lo = 0
    hi = len(height) - 1

    while lo < hi:
        h_lo = height[lo]
        h_hi = height[hi]

        ans = max(ans, (hi - lo) * min(h_lo, h_hi))

        if h_lo <= h_hi:
            lo += 1
        else:
            hi -= 1

    return ans


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
