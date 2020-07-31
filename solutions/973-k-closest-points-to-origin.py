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


def kClosest(points: [[int]], K: int) -> [[int]]:
    hq = []

    for x, y in points:
        d = math.sqrt(math.pow(abs(x), 2) + math.pow(abs(y), 2))
        heapq.heappush(hq, (-d, [x, y]))

        if len(hq) > K:
            heapq.heappop(hq)

    return [p for d, p in hq]


print(kClosest(points=[[1, 3], [-2, 2]], K=1), [[-2, 2]])
print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2), [[3, 3], [-2, 4]])
