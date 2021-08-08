# Remove Stones to Minimize the Total
#
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import heapq
import math


def minStoneSum(piles: List[int], k: int) -> int:
    hq = [-x for x in piles]
    heapq.heapify(hq)

    for _ in range(k):
        cur = -heapq.heappop(hq)
        heapq.heappush(hq, -math.ceil(cur / 2))

    return sum([-x for x in hq])


print(minStoneSum(piles=[5, 4, 9], k=2), 12)
print(minStoneSum(piles=[4, 3, 6, 7], k=3), 12)
