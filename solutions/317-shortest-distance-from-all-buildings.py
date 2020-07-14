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


def shortestDistance(grid: [[int]]) -> int:
    # 1. find start points
    stack = []
    idx = 0
    visited = [[{} for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                stack.append((i, j, idx, 0))
                visited[i][j] = {}
                idx += 1

    # 2. distances
    dist = float("inf")
    while stack:
        i, j, b, d = stack.pop(0)

        if len(visited[i][j]) == idx:
            dist = min(dist, sum(visited[i][j].values()))

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix < 0 or ix >= len(grid) or jy < 0 or jy >= len(grid[0]):
                continue

            if grid[ix][jy] == 0 and b not in visited[ix][jy]:
                stack.append((ix, jy, b, d+1))
                visited[ix][jy][b] = d + 1

    return dist if dist < float("inf") else -1


print(shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), 7)
