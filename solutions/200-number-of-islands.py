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
    if not grid or not grid[0]:
        return 0

    ans = 0
    visited = set()

    def dfs(i, j):
        visited.add((i, j))

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = y + j

            if ix >= 0 and jy >= 0 and ix < len(grid) and jy < len(grid[0]):
                if (ix, jy) not in visited and grid[ix][jy] == "1":
                    dfs(ix, jy)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == "1":
                ans += 1
                dfs(i, j)

    return ans
