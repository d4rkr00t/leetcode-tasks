# Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/
# medium
#
# Tags: Google, Facebook
#
# Time:  O(n^2)
# Space: TBD
#
# Solution:
# TBD

from typing import List
from collections import defaultdict


def minAreaRect(points: List[List[int]]) -> int:
    cols = defaultdict(list)
    ans = float("inf")
    lastx = {}

    for x, y in points:
        cols[x].append(y)

    for x in sorted(cols):
        col = cols[x]
        col.sort()

        for j, y2 in enumerate(col):
            for i in range(j):
                y1 = col[i]
                if (y1, y2) in lastx:
                    ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))

                lastx[y1, y2] = x

    return ans if ans < float("inf") else 0


print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]), 4)
print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]), 2)
