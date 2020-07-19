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

def maxArea(height: [int]) -> int:
    max_area = 0
    lo = 0
    hi = len(height) - 1

    while lo < hi:
        max_area = max(max_area, min(height[lo], height[hi]) * (hi-lo))

        if height[lo] > height[hi]:
            hi -= 1
        else:
            lo += 1

    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
