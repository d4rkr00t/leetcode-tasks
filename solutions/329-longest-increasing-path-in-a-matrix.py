# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# hard
#
# Tags: Google, Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    dp = {}
    ans = 0

    def inBounds(x, y):
        return x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0])

    def dfs(x, y):
        nonlocal ans, dp
        if (x, y) in dp:
            return dp[x, y]

        tmp = 1

        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = j + y
            if inBounds(ix, jy) and matrix[ix][jy] > matrix[x][y]:
                tmp = max(tmp, dfs(ix, jy) + 1)

        dp[x, y] = tmp
        ans = max(ans, tmp)
        return tmp

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            dfs(x, y)

    return ans


print(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)

print(longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]), 4)
