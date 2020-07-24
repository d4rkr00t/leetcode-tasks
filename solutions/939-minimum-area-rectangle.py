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

import collections


def minAreaRect(points: [[int]]) -> int:
    cols = collections.defaultdict(list)

    for x, y in points:
        cols[x].append(y)

    lastx = {}
    area = float("inf")

    for x in sorted(cols):
        col = cols[x]
        col.sort()

        for j, y2 in enumerate(col):
            for i in range(j):
                y1 = col[i]
                if (y1, y2) in lastx:
                    area = min(area, (x-lastx[y1, y2]) * (y2 - y1))

                lastx[y1, y2] = x

    return area if area < float("inf") else 0


print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]), 4)
print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]), 2)

# (1,1) (1,3)
#    (2,2)
# (3,1) (3,3)

# (1,1) (1,3)
# (3,1) (3,3)
# (4,1) (4,3)
