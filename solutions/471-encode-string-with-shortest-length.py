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

    for i in range(n):
        dp[i][i] = s[i:i + 1]

    def repeatIdx(s):
        return (s + s).find(s, 1)

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            tmp = s[i:j + 1]
            dp[i][j] = tmp

            idx = repeatIdx(tmp)
            if idx:
                repeats = len(tmp) // idx
                encodeStr = str(repeats) + "[" + dp[i][i + idx - 1] + "]"

                if len(encodeStr) <= len(dp[i][j]):
                    dp[i][j] = encodeStr

                for k in range(i, j):
                    if len(dp[i][j]) >= (len(dp[i][k]) + len(dp[k + 1][j])):
                        dp[i][j] = dp[i][k] + dp[k + 1][j]

    return dp[0][-1]


print(encode("aaa"), "aaa")
print(encode("aaaaa"), "5[a]")
print(encode("aaaaaaaaaa"), "10[a]")
print(encode("aaaaabb"), "5[a]bb")

# a a a a a b b
# a aa aaa 4[a] 5[a] 5[a]b 5[a]bb
#   a  aa  aaa  4[a] 4[a]b 4[a]bb
#      a   aa   aaa  aaab  aaabb
#          a    aa   aab   aabb
#               a    ab    abb
#                    b     bb
#                          b
