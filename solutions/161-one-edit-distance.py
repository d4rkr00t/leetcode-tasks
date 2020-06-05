# One Edit Distance
# https://leetcode.com/problems/one-edit-distance/
# medium
#
# Tags: Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# DP

def isOneEditDistance(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False

    dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

    for i in range(len(t)):
        dp[i+1][0] = i + 1

    for j in range(len(s)):
        dp[0][j+1] = j + 1

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            substitutionCost = 1
            if s[j-1] == t[i-1]:
                substitutionCost = 0

            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + substitutionCost)

    print(dp)

    return dp[-1][-1] == 1

print(isOneEditDistance(s = "ab", t = "acb"), True)
print(isOneEditDistance(s = "cab", t = "ad"), False)
print(isOneEditDistance(s = "1203", t = "1213"), True)
print(isOneEditDistance("aaaaaaaaa", "aaaaaaaaaa"), True)

#   a a a a a a a a a
#   0 1 2 3 4 5 6 7 8
# a 1 1 1
# a 2
# a 3
# a 4
# a 5
# a 6
# a 7
# a 8
# a 9
# a 10

#     a b
#   0 1 2
# a 1 0 2
# c 2
# b 3

# [[0, 1, 2],
#  [1, 0, 1],
#  [2, 1, 2],
#  [3, 2, 2]
# ]

[
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [2, 0, 0, 1, 2, 3, 4, 5, 6, 7],
    [3, 0, 0, 0, 1, 2, 3, 4, 5, 6],
    [4, 0, 0, 0, 0, 1, 2, 3, 4, 5],
    [5, 0, 0, 0, 0, 0, 1, 2, 3, 4],
    [6, 0, 0, 0, 0, 0, 0, 1, 2, 3],
    [7, 0, 0, 0, 0, 0, 0, 0, 1, 2],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
