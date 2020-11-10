# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  O(n*log(k))
# Space: O(K)

from typing import List
import heapq


def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    hq = []

    for x, y in points:
        d = x**2 + y**2
        heapq.heappush(hq, (-d, x, y))

        if len(hq) > K:
            heapq.heappop(hq)

    return [[x, y] for _, x, y in hq]


print(kClosest(points=[[1, 3], [-2, 2]], K=1), [[-2, 2]])
print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2), [[3, 3], [-2, 4]])
