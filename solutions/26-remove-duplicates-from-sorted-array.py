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

    for n in nums:
        if n == nums[lo]:
            continue

        lo += 1
        nums[lo] = n

    return lo + 1


print(removeDuplicates([1, 1, 2]), 2)
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)

#         lo
#   0, 1, 2, 1, 2, 2, 3, 3, 4, 4
#                     |
