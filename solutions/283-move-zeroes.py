# Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# easy
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    lo = -1
    for hi in range(len(nums)):
        if nums[hi] == 0 and lo == -1:
            lo = hi

        if nums[hi] != 0 and lo != -1:
            nums[hi], nums[lo] = nums[lo], nums[hi]
            lo += 1

    return nums


print(moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
