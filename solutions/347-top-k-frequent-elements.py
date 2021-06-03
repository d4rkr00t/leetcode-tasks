# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(n*log(k))
# Space: O(n)
#
# Solution:
# TBD

from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    table = {}

    for n in nums:
        table[n] = table.get(n, 0) + 1

    hq = []
    for (num, count) in table.items():
        heapq.heappush(hq, (count, num))
        if len(hq) > k:
            heapq.heappop(hq)

    return [num for (_, num) in hq]


print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2), [1, 2])
print(topKFrequent(nums=[1], k=1), [1])
