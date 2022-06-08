# Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from re import L
from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    ans = 0

    def inBounds(x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    def dfs(x, y):
        closed = True
        grid[x][y] = 2

        for i, j, in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            xi = x + i
            yj = y + j
            if inBounds(xi, yj):
                if grid[xi][yj] == 0 and not dfs(xi, yj):
                    closed = False
            else:
                closed = False

        return closed

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                if dfs(x, y):
                    ans += 1

    return ans


print(
    closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0],
                  [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0]]), 2)

print(closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]), 1)

print(
    closedIsland([[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1]]), 2)
