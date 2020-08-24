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
    lo = hi = 0

    while hi < len(nums):
        if nums[hi] == nums[lo]:
            hi += 1
        else:
            if lo+1 < hi:
                nums[lo+1], nums[hi] = nums[hi], nums[lo+1]
            lo += 1
            hi += 1

    return lo + 1


print(removeDuplicates([1, 1, 2]), 2)
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
# 0, 0, 1, 1, 1, 2, 2, 3, 3, 4
# |     |
# 0, 1, 1, 1, 1, 2, 2, 3, 3, 4
# |  |
