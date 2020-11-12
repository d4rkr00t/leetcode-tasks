# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# medium
#
# Tags: Amazon, Google
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers

from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    ans = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        ans = max(ans, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
