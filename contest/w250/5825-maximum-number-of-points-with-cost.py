# Maximum Number of Points with Cost
# https://leetcode.com/contest/weekly-contest-250/problems/maximum-number-of-points-with-cost/
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


def maxPoints(points: List[List[int]]) -> int:
    m = len(points[0])
    cur = points[0]
    ans = max(cur)
    for i in range(1, len(points)):
        next = [0] * m
        for j in range(m):
            lo = max(j - points[i][j], 0)
            hi = min(j + points[i][j], m - 1)
            for k in range(lo, hi + 1):
                next[j] = max(next[j], cur[k] + points[i][j] - abs(k - j))
                ans = max(ans, next[j])
        cur = next

    return ans


print(maxPoints([[4, 1], [0, 0], [5, 5], [0, 1], [0, 0]]), 9)
print(maxPoints([[5, 2, 1, 2], [2, 1, 5, 2], [5, 5, 5, 0]]), 13)
print(maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]), 9)
print(maxPoints([[1, 5], [2, 3], [4, 2]]), 11)

# 4 1
# 0 0
# 5 5
# 0 1
# 0 0

# 4 1
# 4 1
# 9 8
# 9 9
# 9 9
