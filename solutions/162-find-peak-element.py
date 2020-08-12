# Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findPeakElement(nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    return lo


print(findPeakElement([1, 2, 3, 1]), 2)
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]), 1, 5)
