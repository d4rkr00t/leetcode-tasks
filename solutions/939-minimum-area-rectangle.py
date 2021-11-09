# Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/
# medium
#
# Tags: Google, Facebook
#
# Time:  TBD
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


# cols = {1:[1,3], 2:[2], 3:[1,3]}
# x = 1
# col = [1,3]
# j = 0
# i = 0
# y2 = 1
# y1 = 1
# lastx = {(1,1): 1}
# ----------
# x = 1
# col = [1,3]
# j = 0
# i = 1
# y2 = 1
# y1 = 3
# lastx = {(1,1): 1, (3,1): 1}
# ----------
# x = 1
# col = [1,3]
# j = 1
# i = 0
# y2 = 3
# y1 = 1
# lastx = {(1,1): 1, (3,1): 1, (1,3): 1}
# ----------
# x = 2
# col = [2]
# j = 0
# i = 0
# y2 = 2
# y1 = 2
# lastx = {(1,1): 1, (3,1): 1, (1,3): 1, (2,2): 2}
# ----------
# x = 3
# col = [1,3]
# j = 0
# i = 0
# y2 = 1
# y1 = 1
# lastx = {(1,1): 1, (3,1): 1, (1,3): 1, (2,2): 2}
# ans =

print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]), 4)
print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]), 2)
