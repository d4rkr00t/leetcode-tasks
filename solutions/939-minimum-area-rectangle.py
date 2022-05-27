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

from collections import defaultdict
from typing import List


def minAreaRect(points: List[List[int]]) -> int:
    points.sort()
    rows = defaultdict(set)
    cols = defaultdict(set)
    ans = float("inf")

    for row, col in points:
        for srow in cols[col]:
            for scol in rows[srow]:
                if (row, col) != (row, scol):
                    if scol in rows[row] and scol in rows[
                            srow] and srow in cols[col]:
                        ans = min(ans, abs(srow - row) * abs(scol - col))

        rows[row].add(col)
        cols[col].add(row)

    return ans if ans != float("inf") else 0


# row = 3, col = 3
# srow = 1, scol = 1
# (3,3), (3,1), (1,1), (1,3)
# (row, col), (row,scol), (srow,scol), (srow,col)

print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]), 4)
print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]), 2)

# [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
# rows: {
#   1: [1,3]
#   2: [2]
#   3: [1, 3]
# }
# cols: {
#   1: [1, 3]
#   2: [2]
#   3: [1, 3]
# }
