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
    islands = 0

    def inbounds(x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    def dfs(i, j):
        grid[i][j] = "#"

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            xi = x + i
            yj = y + j

            if inbounds(xi, yj) and grid[xi][yj] == "1":
                dfs(xi, yj)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                islands += 1
                dfs(i, j)

    return islands
