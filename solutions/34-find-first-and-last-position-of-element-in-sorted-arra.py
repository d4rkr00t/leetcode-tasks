# Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# medium
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def bsearch(lo, hi):
        if lo > hi:
            return -1

        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return bsearch(lo, mid - 1)

        return bsearch(mid + 1, hi)

    idx = bsearch(0, len(nums) - 1)
    if idx == -1:
        return [-1, -1]

    left = maybe_left = idx
    while maybe_left != -1:
        maybe_left = bsearch(0, left - 1)
        if maybe_left != -1:
            left = maybe_left

    right = maybe_right = idx
    while maybe_right != -1:
        maybe_right = bsearch(right + 1, len(nums) - 1)
        if maybe_right != -1:
            right = maybe_right

    return [left, right]


print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8), [3, 4])
print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=6), [-1, -1])

# [5, 7, 7, 8, 8, 10]
#              |
#        |        |
