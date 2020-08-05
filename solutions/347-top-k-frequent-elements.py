# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from heapq import heappop
from typing import List

import heapq
import collections


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = collections.Counter(nums)
    hq = []

    for key in counts.keys():
        heapq.heappush(hq, (counts[key], key))

        if len(hq) > k:
            heapq.heappop(hq)

    return [n for c, n in hq]


print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2), [1, 2])
print(topKFrequent(nums=[1], k=1), [1])
