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
    ans = 0
    n, m = len(matrix), len(matrix[0])
    cache = [[0] * m for _ in range(n)]

    def dfs(i, j):
        nonlocal ans, cache

        if cache[i][j]:
            return cache[i][j]

        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and jy >= 0 and ix < n and jy < m and matrix[ix][
                    jy] < matrix[i][j]:
                cache[i][j] = max(dfs(ix, jy), cache[i][j])

        cache[i][j] += 1
        return cache[i][j]

    visited = set()
    for i in range(n):
        for j in range(m):
            ans = max(dfs(i, j), ans)

    return ans


print(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)

print(longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]), 4)
