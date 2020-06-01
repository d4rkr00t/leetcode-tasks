# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# hard
#
# Tags: Google, Facebook, Amazon
#
# Time:  O(m*n)
# Space: if not matrix: return 0
#
# Solution:
# DFS + cache

def longestIncreasingPath(matrix: [[int]]) -> int:
    if not matrix: return 0

    n = len(matrix)
    m = len(matrix[0])
    cache = [[0] * m for _ in range(n)]

    def dfs(i,j):
        nonlocal cache, matrix, n, m

        if cache[i][j]: return cache[i][j]

        for di,dj in [(-1,0), (0,1), (1,0), (0, -1)]:
            ni = i + di
            nj = j + dj

            if ni >= 0 and ni < n and nj >= 0 and nj < m and matrix[ni][nj] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], dfs(ni, nj))

        cache[i][j] += 1
        return cache[i][j]

    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ans = max(ans, dfs(i, j))

    return ans


print(longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
]), 4)

print(longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
]), 4)
