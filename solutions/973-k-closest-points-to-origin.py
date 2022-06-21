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

import heapq
import math
from typing import List


def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    def dist(point):
        return math.sqrt(point[0]**2 + point[1]**2)

    hq = []

    for point in points:
        d = dist(point)
        heapq.heappush(hq, (-d, point))
        if len(hq) > K:
            heapq.heappop(hq)

    return [p for _, p in hq]


print(kClosest(points=[[1, 3], [-2, 2]], K=1), [[-2, 2]])
print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2), [[3, 3], [-2, 4]])
