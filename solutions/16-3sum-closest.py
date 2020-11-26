# 3Sum Closest
# https://leetcode.com/problems/3sum-closest/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  O(n^2)
# Space: O(1)
#
# Solution:
# Two pointes

from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    diff = float("inf")
    nums.sort()

    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1

        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - sum) < abs(diff):
                diff = target - sum

            if sum < target:
                lo += 1
            else:
                hi -= 1

        if diff == 0:
            break

    return target - diff


print(threeSumClosest(nums=[-1, 2, 1, -4], target=1), 2)
"""
-1, 2, 1, -4
^          ^
"""
