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
    lo = 0
    for i in range(len(nums)):
        n = nums[i]
        if nums[lo] != 0 and n == 0:
            lo = i

        if lo != -1 and n != 0:
            nums[i], nums[lo] = nums[lo], nums[i]
            lo = lo + 1

    return nums


print(moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
print(moveZeroes([0, 1, 0, 3, 0, 0, 12]), [1, 3, 12, 0, 0, 0, 0])
#   0, 0, 1, 3, 0, 0, 12
