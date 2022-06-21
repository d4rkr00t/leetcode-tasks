# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# hard
#
# Tags: Google, Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import deque
from typing import List


def shortestPath(grid: List[List[int]], k: int) -> int:
    visited = set([(0, 0, k)])
    n = len(grid) - 1
    m = len(grid[0]) - 1
    queue = deque([(0, 0, k, 0)])

    def inBounds(x, y):
        return x >= 0 and x <= n and y >= 0 and y <= m

    while queue:
        x, y, r, d = queue.popleft()

        if x == n and y == m:
            return d

        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = j + y
            if not inBounds(ix, jy): continue

            nr = r - 1 if grid[ix][jy] == 1 else r

            if (ix, jy, nr) not in visited and nr >= 0:
                visited.add((ix, jy, nr))
                queue.append((ix, jy, nr, d + 1))

    return -1


print(
    shortestPath(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]],
                 k=1), 6)

print(shortestPath(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1), -1)

print(
    shortestPath(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 0, 1, 1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]], 1),
    20)
