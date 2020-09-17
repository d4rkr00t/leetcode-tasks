# Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def search(nums: List[int], target: int) -> int:
    def find_pivot(nums):
        if nums[0] < nums[-1]:
            return -1

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] < nums[0]:
                hi = mid
            else:
                lo = mid

        return -1

    def bsearch(nums, lo, hi):
        mid = (lo+hi) // 2

        if lo > hi:
            return -1

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return bsearch(nums, lo, mid-1)

        if nums[mid] < target:
            return bsearch(nums, mid+1, hi)

    pivot = find_pivot(nums)

    if pivot == -1:
        return bsearch(nums, 0, len(nums)-1)

    left = bsearch(nums, 0, pivot)
    right = bsearch(nums, pivot+1, len(nums)-1)

    return max(left, right)


print(search([4, 5, 6, 7, 0, 1, 2, 3], 0), 4)
print(search([4, 5, 6, 7, 0, 1, 2], 3), -1)
print(search([5, 1, 3], 5), 0)

# 4 5 6 7 0 1 2 3
#     | | |
