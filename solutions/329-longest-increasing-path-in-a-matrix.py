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
    if not matrix:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    ans = 0
    cache = [[0] * m for _ in range(n)]

    def dfs(i, j):
        nonlocal n, m, cache

        if cache[i][j]:
            return cache[i][j]

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = x + i
            jy = y + j

            if ix >= 0 and jy >= 0 and ix < n and jy < m and matrix[i][j] < matrix[ix][jy]:
                cache[i][j] = max(cache[i][j], dfs(ix, jy))

        cache[i][j] += 1
        return cache[i][j]

    for i in range(n):
        for j in range(m):
            ans = max(ans, dfs(i, j))

    return ans


print(longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]), 4)

print(longestIncreasingPath([
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]), 4)
