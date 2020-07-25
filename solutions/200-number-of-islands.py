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

def numIslands(self, grid: [[str]]) -> int:
    count = 0

    def dfs(i, j):
        grid[i][j] = "2"

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and ix < len(grid) and jy >= 0 and jy < len(grid[0]):
                if grid[ix][jy] == "1":
                    dfs(ix, jy)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)

    return count
