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

from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    hq = []

    for n in nums:
        heapq.heappush(hq, n)

        if len(hq) > k:
            heapq.heappop(hq)

    return heapq.nlargest(k, hq)[-1]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
