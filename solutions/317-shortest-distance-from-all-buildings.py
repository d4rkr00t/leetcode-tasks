# Shortest Distance from All Buildings
# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# hard
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  O((E+V) * B)
# Space: O(E+V)
#
# Solution:
# BFS

def shortestDistance(grid: [[int]]) -> int:
    stack = []
    buildings = 0
    visited = [[{} for _ in  range(len(grid[0]))] for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                stack.append((i,j,(i,j),0))
                buildings += 1

    dist = float("inf")
    while stack:
        i,j,b,d = stack.pop(0)

        for x,y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and ix < len(grid) and jy >= 0 and jy < len(grid[0]) and grid[ix][jy] == 0:
                if not b in visited[ix][jy]:
                    visited[ix][jy][b] = d+1
                    stack.append((ix, jy, b, d+1))

                    if len(visited[ix][jy].keys()) == buildings:
                        dist = min(sum(visited[ix][jy].values()), dist)

    return dist if dist < float("inf") else -1


print(shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]), 7)
