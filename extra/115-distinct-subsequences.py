# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def numDistinct(s: str, t: str) -> int:
    dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

    for i in range(len(s) + 1):
        dp[0][i] = 1

    for i in range(len(t)):
        for j in range(len(s)):
            if t[i] == s[j]:
                dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i + 1][j]

    return dp[-1][-1]


print(numDistinct(s="rabbbit", t="rabbit"), 3)
print(numDistinct(s="babgbag", t="bag"), 5)

#     b a b g b a g
#   1 1 1 1 1 1 1 1
# b 0 1 1 2 2 3 3 3
# a 0 0 1 1 1 1 4 4
# g 0 0 0 0 1 1 1 5

#     b a g
#   0 0 0 0
# b 0
# a 0
# b 0
# g 0
# b 0
# a 0
# g 0
