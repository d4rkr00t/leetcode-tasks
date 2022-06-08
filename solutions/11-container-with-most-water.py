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
        loH = height[lo]
        hiH = height[hi]
        ans = max(ans, min(loH, hiH) * (hi - lo))
        if loH < hiH:
            lo += 1
        else:
            hi -= 1

    return ans


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
