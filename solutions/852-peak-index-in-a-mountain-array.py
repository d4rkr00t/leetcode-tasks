# Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# easy
#
# Tags: Facebook, Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return hi


print(peakIndexInMountainArray([0, 1, 0]), 1)
print(peakIndexInMountainArray([0, 2, 1, 0]), 1)

# 0 1 2 3 2 5
#     l   h
