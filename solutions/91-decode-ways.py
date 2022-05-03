# Decode Ways
# https://leetcode.com/problems/decode-ways/
# medium
#
# Tags: Aamzon, Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def numDecodings(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    dp = [None] * n

    def recur(pos):
        if pos == n:
            return 1

        if dp[pos] != None:
            return dp[pos]

        cur = s[pos]

        if cur == "0":
            return 0

        ways = recur(pos + 1)

        if pos + 1 < n:
            cur += s[pos + 1]
            if int(cur) <= 26:
                ways += recur(pos + 2)

        dp[pos] = ways

        return ways

    return recur(0)


print(numDecodings("12"), 2)
print(numDecodings("226"), 3)
