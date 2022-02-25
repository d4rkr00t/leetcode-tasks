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
    def findPivot(arr, lo, hi):
        while hi - lo > 1:
            mid = (lo + hi) // 2

            if arr[mid] > arr[hi]:
                lo = mid
            else:
                hi = mid

        return lo

    def bsearch(arr, lo, hi, target):
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    pivot = findPivot(nums, 0, len(nums) - 1)
    left = bsearch(nums, 0, pivot, target)
    right = bsearch(nums, pivot + 1, len(nums) - 1, target)

    return max(left, right)


print(search([4, 5, 6, 7, 0, 1, 2], 0), 4)
print(search([4, 5, 6, 7, 0, 1, 2], 3), -1)
print(search([1, 2, 3], 2), 1)
print(search([4, 1, 2, 3], 2), 2)
print(search([2, 1], 2), 0)

# [4, 5, 6, 7, 0, 1, 2]
#  |        |        |
# [1, 2, 3]
#        p
# [4, 1, 2, 3]
#  p
# [2, 1]
#  p
