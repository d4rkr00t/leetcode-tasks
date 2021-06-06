# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# easy
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  O(n)
# Space: O(1)

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    lo = 0

    for hi, n in enumerate(nums):
        if nums[lo] == nums[hi]:
            continue

        lo += 1

        nums[lo], nums[hi] = nums[hi], nums[lo]

    return lo + 1


print(removeDuplicates([1, 1, 2]), 2)
print(removeDuplicates([1, 2, 3]), 3)
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)

#  0, 1, 2, 1, 1, 2, 2, 3, 3, 4
#        ^              ^
