# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# medium
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  O(n*log(n))
# Space: O(1)
#
# Solution:
# TBD

from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
