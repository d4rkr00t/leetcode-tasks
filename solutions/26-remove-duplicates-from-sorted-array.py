# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# easy
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    lo = 0

    for hi, n in enumerate(nums):
        if lo == hi:
            continue

        if nums[lo] != nums[hi]:
            lo += 1
            nums[hi], nums[lo] = nums[lo], nums[hi]

    return nums


print(removeDuplicates([1, 1, 2]), 2)
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)

# 0 1 2 3 4 5
#           |
#           |
