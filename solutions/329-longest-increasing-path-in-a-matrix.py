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

def longestIncreasingPath(matrix: [[int]]) -> int:
    ans = 0
    cache = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    def dfs(i, j):
        if cache[i][j] != 0:
            return cache[i][j]

        for x,y in [(-1,0), (0,1), (1, 0), (0, -1)]:
            ix = i + x
            jy = j + y

            if ix >= 0 and ix < len(matrix) and jy >= 0 and jy < len(matrix[0]) and matrix[ix][jy] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], dfs(ix, jy))

        cache[i][j] += 1
        return cache[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
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
