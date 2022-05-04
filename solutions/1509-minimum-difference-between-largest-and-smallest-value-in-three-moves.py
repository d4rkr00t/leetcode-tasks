# Minimum Difference Between Largest and Smallest Value in Three Moves
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def minDifference(nums: List[int]) -> int:
    if len(nums) <= 4:
        return 0

    nums.sort()
    n = len(nums)
    diff = float("inf")

    for i in range(4):
        diff = min(diff, abs(nums[i] - nums[n - (3 - i) - 1]))

    return diff


print(minDifference([5, 3, 2, 4]), 0)
print(minDifference([1, 5, 0, 10, 14]), 1)
print(minDifference([6, 6, 0, 1, 1, 4, 6]), 2)
print(minDifference([1, 5, 6, 14, 15]), 1)
print(minDifference([20, 66, 68, 57, 45, 18, 42, 34, 37, 58]), 31)

# 0, 1, 1, 4, 6, 6, 6
#          |        |
