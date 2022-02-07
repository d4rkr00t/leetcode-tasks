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

from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    n = len(grid)
    m = len(grid[0])

    def isAtEdge(i, j):
        return i == 0 or j == 0 or i + 1 == n or j + 1 == m

    def inboundary(i, j):
        return i >= 0 and i < n and j >= 0 and j < m

    def dfs(i, j):
        at_edge = isAtEdge(i, j)

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            xi = i + x
            yj = j + y

            if inboundary(xi, yj) and grid[xi][yj] == 0:
                grid[xi][yj] = 2
                res = dfs(xi, yj)
                at_edge = res if not at_edge else at_edge

        return at_edge

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                ans += 1 if not dfs(i, j) else 0

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
