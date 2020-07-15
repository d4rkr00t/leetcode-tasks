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

def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    lo = hi = 0

    while hi < len(nums):
        if nums[hi] != 0 and nums[lo] == 0:
            nums[hi], nums[lo] = nums[lo], nums[hi]

        while nums[lo] != 0:
            lo += 1
            hi = max(lo, hi)

        hi += 1

    return nums


print(moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
