# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# hard
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(1)

from typing import List


def trap(height: List[int]) -> int:
    lo, hi = 0, len(height) - 1
    mlo, mhi = height[lo], height[hi]
    ans = 0

    while lo < hi:
        ans += min(mlo, mhi) - min(height[hi], height[lo])

        if height[lo] >= height[hi]:
            hi -= 1
            mhi = max(mhi, height[hi])
        else:
            lo += 1
            mlo = max(mlo, height[lo])

    return ans


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
print(trap([0, 1, 2, 3]), 0)
print(trap([0, 1, 0, 1]), 1)
"""
              3
      2       3 2   2
_ 1 _ 2 1 _ 1 3 2 1 2 1
      ^           ^
      lo          hi

mlo = 2
mhi = 2
ans = 1
"""
