# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(n * log(k))
# Space: O(n)
#
# Solution:
# TBD

import heapq

def topKFrequent(nums: [int], k: int) -> [int]:
    pq = []
    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    for n in freq.keys():
        heapq.heappush(pq, (freq[n], n))

        if len(pq) > k:
            heapq.heappop(pq)

    return [n for f,n in pq]

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2), [1,2])
print(topKFrequent(nums = [1], k = 1), [1])
