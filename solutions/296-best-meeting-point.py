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
    if not grid:
        return 0
    r, c = len(grid), len(grid[0])
    sumr = [i for i in range(r) for j in range(c) if grid[i][j]]
    sumc = [j for i in range(r) for j in range(c) if grid[i][j]]
    sumr.sort()
    sumc.sort()
    mid_row = sumr[len(sumr)//2]
    mid_col = sumc[len(sumc)//2]
    return sum([abs(r-mid_row) for r in sumr]) + sum([abs(c-mid_col) for c in sumc])


print(minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), 6)
