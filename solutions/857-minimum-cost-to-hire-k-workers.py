# Minimum Cost to Hire K Workers
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import heapq


def mincostToHireWorkers(quality: List[int], wage: List[int], K: int) -> float:
    workers = sorted([(w / q, q, w) for q, w in zip(quality, wage)])
    ans = float("inf")
    pool = []
    sumq = 0

    for ratio, q, w in workers:
        heapq.heappush(pool, -q)
        sumq += q

        if len(pool) > K:
            sumq += heapq.heappop(pool)

        if len(pool) == K:
            ans = min(ans, ratio * sumq)

    return float(ans)


print(mincostToHireWorkers(
    quality=[10, 20, 5], wage=[70, 50, 30], K=2), 105.00000)
print(mincostToHireWorkers(
    quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], K=3), 30.66667)
