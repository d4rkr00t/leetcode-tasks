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
import collections


def shortestDistance(grid: List[List[int]]) -> int:
    buildings = []
    visited = collections.defaultdict(dict)
    ans = float("inf")

    def dist(x, y):
        return sum([abs(x1 - x) + abs(y1 - y) for x1, y1, _ in buildings])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                buildings.append((i, j, set([(i, j)])))

    queue = list(buildings)
    while queue:
        i, j, cur_visited = queue.pop(0)

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y
            if ix < 0 or ix >= len(grid) or jy < 0 or jy >= len(grid[0]):
                continue

            if (ix, jy) not in cur_visited and grid[ix][jy] == 0:
                visited[ix][jy] = visited[ix].get(jy, 0) + 1
                if visited[ix][jy] == len(buildings):
                    ans = min(ans, dist(ix, jy))
                cur_visited.add((ix, jy))
                queue.append((ix, jy, cur_visited))

    return ans if ans != float("inf") else -1


print(shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), 7)
[[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0,
                                          1], [1, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]
