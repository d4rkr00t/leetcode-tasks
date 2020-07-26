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

import collections
import heapq


def topKFrequent(nums: [int], k: int) -> [int]:
    freq = collections.defaultdict(int)
    hq = []

    for n in nums:
        freq[n] += 1

    for n in freq.keys():
        heapq.heappush(hq, (freq[n], n))

        if len(hq) > k:
            heapq.heappop(hq)

    return [n for _, n in hq]


print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2), [1, 2])
print(topKFrequent(nums=[1], k=1), [1])
