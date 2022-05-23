# Best Meeting Point
# https://leetcode.com/problems/best-meeting-point/
# hard
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def minTotalDistance(grid: List[List[int]]) -> int:
    rows = []
    cols = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                rows.append(row)
                cols.append(col)

    def minDist(points, origin):
        dist = 0

        for p in points:
            dist += abs(origin - p)

        return dist

    row = rows[len(rows) // 2]
    cols.sort()
    col = cols[len(cols) // 2]

    return minDist(rows, row) + minDist(cols, col)


print(minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), 6)
