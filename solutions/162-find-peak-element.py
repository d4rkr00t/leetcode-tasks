# Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(log(n))
# Space: O(1)
#
# Solution:
# Binary Search

from typing import List


def findPeakElement(nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = (hi + lo) >> 1

        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    return hi


print(findPeakElement([1, 2, 3, 1]), 2)
print(findPeakElement([1, 2]), 1)
print(findPeakElement([3, 2, 1]), 0)
print(findPeakElement([1, 2, 1, 2, 3, 4, 5]), 1, 6)
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]), 1, 5)
