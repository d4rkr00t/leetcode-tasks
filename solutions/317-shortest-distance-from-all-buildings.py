# Shortest Distance from All Buildings
# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# hard
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def shortestDistance(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    buildings = []
    dists = [[(0, 0)] * m for _ in range(n)]
    ans = float("inf")

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                buildings.append((i, j))

    def bfs(i, j):
        nonlocal ans
        visited = set((i, j))
        queue = [(i, j, 0)]

        while queue:
            x, y, d = queue.pop(0)
            visited_by, cur_dist = dists[x][y]

            if visited_by == len(buildings):
                ans = min(ans, cur_dist)

            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and ny >= 0 and nx < n and ny < m and (
                        nx, ny) not in visited and grid[nx][ny] == 0:
                    dists[nx][ny] = (dists[nx][ny][0] + 1,
                                     dists[nx][ny][1] + d + 1)
                    queue.append((nx, ny, d + 1))
                    visited.add((nx, ny))

    for i, j in buildings:
        bfs(i, j)

    return ans if ans < float("inf") else -1


print(shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), 7)
