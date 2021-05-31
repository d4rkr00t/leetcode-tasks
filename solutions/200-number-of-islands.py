# Number of Islands
# https://leetcode.com/problems/number-of-islands/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def numIslands(self, grid: List[List[str]]) -> int:
    def expand(grid, i, j):
        queue = [(i, j)]

        while queue:
            (i, j) = queue.pop(0)

            for (x, y) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ix = i + x
                jy = j + y

                if ix >= 0 and ix < len(grid) and jy >= 0 and jy < len(
                        grid[0]) and grid[ix][jy] == "1":
                    grid[ix][jy] = "X"
                    queue.append((ix, jy))

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                ans += 1
                grid[i][j] = "X"
                expand(grid, i, j)

    return ans
