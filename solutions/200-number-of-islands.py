# Number of Islands
# https://leetcode.com/problems/number-of-islands/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(N*M)
# Space: O(1)
#
# Solution:
# Connected Components

def numIslands(self, grid: [[str]]) -> int:
    def dfs(i, j):
        nonlocal grid

        grid[i][j] = "2"

        for di,dj in [(-1,0), (1,0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == "1":
                dfs(ni, nj)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)

    return count
