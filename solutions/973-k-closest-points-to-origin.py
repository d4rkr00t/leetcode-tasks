# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import heapq
import math


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    hq = []

    for x, y in points:
        dist = math.sqrt(x**2 + y**2)
        heapq.heappush(hq, (-dist, x, y))

        if len(hq) > k:
            heapq.heappop(hq)

    return [(x, y) for _, x, y in hq]


print(kClosest(points=[[1, 3], [-2, 2]], K=1), [[-2, 2]])
print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2), [[3, 3], [-2, 4]])
