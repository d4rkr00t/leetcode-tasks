# Minimum Difference Between Largest and Smallest Value in Three Moves
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def minDifference(nums: List[int]) -> int:
    if len(nums) < 5:
        return 0

    lo = 0
    hi = len(nums) - 4
    nums.sort()

    ans = float("inf")

    while hi < len(nums):
        ans = min(ans, nums[hi] - nums[lo])

        lo += 1
        hi += 1

    return ans


print(minDifference([5, 3, 2, 4]), 0)
print(minDifference([1, 5, 0, 10, 14]), 1)
print(minDifference([6, 6, 0, 1, 1, 4, 6]), 2)
print(minDifference([1, 5, 6, 14, 15]), 1)
print(minDifference([20, 66, 68, 57, 45, 18, 42, 34, 37, 58]), 31)
