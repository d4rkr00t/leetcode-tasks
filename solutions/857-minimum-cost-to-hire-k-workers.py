# Minimum Cost to Hire K Workers
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# hard
#
# Tags: Google
#
# Time:  O(n log k)
# Space: O(k)
#
# Solution:
# TBD

import heapq

def mincostToHireWorkers(quality: [int], wage: [int], K: int) -> float:
    workers = sorted((w/q, q, w,) for q, w in zip(quality, wage))

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

    return ans

print(mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], K = 2), 105.00000)
print(mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3), 30.66667)


# 0
# 70, 100, 35
#
