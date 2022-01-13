# Encode String with Shortest Length
# https://leetcode.com/problems/encode-string-with-shortest-length/
# hard
#
# Tags: Google, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def encode(s: str) -> str:
    n = len(s)
    dp = [[""] * n for _ in range(n)]

    def getRepeated(s):
        return (s + s).find(s, 1)

    for i in range(n):
        dp[i][i] = s[i:i + 1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            sub = s[i:j + 1]
            dp[i][j] = sub

            rep_len = getRepeated(sub)

            if rep_len > 0:
                count = (j - i + 1) // rep_len
                es = str(count) + '[' + dp[i][i + rep_len - 1] + ']'

                if len(es) < len(sub):
                    dp[i][j] = es

            for k in range(i, j):
                if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k + 1][j]

    return dp[0][-1]


print(encode("aaa"), "aaa")
print(encode("aaaaa"), "5[a]")
print(encode("aaaaaaaaaa"), "10[a]")
print(encode("aaaaabbbaaa"), "5[a]bbbaaa")
print(encode("aabcaabcd"), "2[aabc]d")
print(encode("babcdabcd"), "b2[abcd]")
print(encode("ababab"), "3[ab]")

#   a ab aba abab ababa ababab
#   0  1   2    3     4      5
# 0
# 1
# 2
# 3
# 4
# 5
