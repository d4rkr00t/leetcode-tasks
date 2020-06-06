# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  O(N * log(K))
# Space: O(K)
#
# Solution:
# TBD

import heapq
import math

def kClosest(points: [[int]], K: int) -> [[int]]:
    def dist(point):
        origin = (0, 0)
        return math.sqrt(point[0]**2 + point[1]**2)

    pq = []

    for p in points:
        d = dist(p)
        heapq.heappush(pq, (-d, p))

        if len(pq) > K:
            heapq.heappop(pq)

    return [p for d,p in pq]

print(kClosest(points = [[1,3],[-2,2]], K = 1), [[-2,2]])
print(kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2), [[3,3],[-2,4]])
