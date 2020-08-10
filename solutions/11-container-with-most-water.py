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
    ar, lo, hi = 0, 0, len(height) - 1

    while lo < hi:
        ar = max(ar, min(height[lo], height[hi]) * (hi - lo))

        if height[hi] > height[lo]:
            lo += 1
        else:
            hi -= 1

    return ar


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
