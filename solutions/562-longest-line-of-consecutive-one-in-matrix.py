# Longest Line of Consecutive One in Matrix
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def longestLine(mat: List[List[int]]) -> int:
    ans = 0

    if not mat:
        return ans

    m = len(mat)
    n = len(mat[0])
    dp = [[[None, None, None, None] for _ in range(n)] for _ in range(m)]
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1)]

    def inbounds(x, y):
        return x >= 0 and x < m and y >= 0 and y < n

    def dfs(x, y, d):
        if dp[x][y][d] != None:
            return dp[x][y][d]

        res = 1
        i, j = dirs[d]
        xi = x + i
        yj = y + j

        if inbounds(xi, yj) and mat[xi][yj] == 1:
            res += dfs(xi, yj, d)

        dp[x][y][d] = res
        return res

    for x in range(m):
        for y in range(n):
            if mat[x][y] == 0:
                continue

            for d in range(len(dirs)):
                res = dp[x][y][d]
                if res == None:
                    res = dfs(x, y, d)

                ans = max(ans, res)

    return ans


# print(longestLine([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]), 3)
print(longestLine([[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]]), 4)
print(
    longestLine([[1, 1, 0, 0, 1, 0, 0, 1, 1,
                  0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                 [1, 1, 1, 0, 0, 1, 1, 1, 1,
                  0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 1, 1, 1,
                  0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1, 0, 0,
                  1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                 [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                 [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]), 9)

# [1, 1, 0, 0, 1, 0, 0, 1, 1, 0]
# [1, 0, 0, 1, 0, 1, 1, 1, 1, 1]
# [1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
# [0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 0]
# [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
# [0, 1, 1, 1, 1, 1, 1, 0, 0, 1]
# [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
# [0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
# [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
