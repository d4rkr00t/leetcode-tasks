# 3Sum Closest
# https://leetcode.com/problems/3sum-closest/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    ans = float("inf")
    nums.sort()

    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            s = nums[i] + nums[lo] + nums[hi]

            if abs(target-s) < abs(ans):
                ans = target - s

            if s < target:
                lo += 1
            else:
                hi -= 1

        if ans == 0:
            break

    return target - ans


print(threeSumClosest(nums=[-1, 2, 1, -4], target=1), 2)

# -4 -1 1 2 = -2
#  |      |
