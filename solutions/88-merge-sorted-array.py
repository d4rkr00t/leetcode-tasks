# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# easy
#
# Tags: Facebook, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1
    p2 = n - 1
    hi = m + n

    while hi > 0:
        p1n = nums1[p1] if p1 >= 0 else float("-inf")
        p2n = nums2[p2] if p2 >= 0 else float("-inf")

        if p1n > p2n:
            nums1[hi - 1], nums1[p1] = nums1[p1], nums1[hi - 1]
            p1 -= 1
            hi -= 1
        else:
            nums1[hi - 1], nums2[p2] = nums2[p2], nums1[hi - 1]
            p2 -= 1
            hi -= 1

    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6])

# 1 4 0 0 0 6
#   |     |
# 1 2 3 5
#       |
