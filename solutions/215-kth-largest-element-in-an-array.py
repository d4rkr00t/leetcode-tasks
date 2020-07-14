# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# medium
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import heapq


def findKthLargest(nums: [int], k: int) -> int:
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
