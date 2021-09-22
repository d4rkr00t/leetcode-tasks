# Largest Plus Sign
# https://leetcode.com/problems/largest-plus-sign/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    ans = 0
    banned = {tuple(mine) for mine in mines}
    dp = [[0] * n for _ in range(n)]

    for r in range(n):
        count = 0
        for c in range(n):
            count = 0 if (r, c) in banned else count + 1
            dp[r][c] = count

        count = 0
        for c in range(n - 1, -1, -1):
            count = 0 if (r, c) in banned else count + 1
            if count < dp[r][c]: dp[r][c] = count

    for c in range(n):
        count = 0
        for r in range(n):
            count = 0 if (r, c) in banned else count + 1
            if count < dp[r][c]: dp[r][c] = count

        count = 0
        for r in range(n - 1, -1, -1):
            count = 0 if (r, c) in banned else count + 1
            if count < dp[r][c]: dp[r][c] = count
            ans = max(ans, dp[r][c])

    return ans


print(orderOfLargestPlusSign(n=5, mines=[[4, 2]]), 2)
# print(orderOfLargestPlusSign(n=1, mines=[[0, 0]]), 0)
