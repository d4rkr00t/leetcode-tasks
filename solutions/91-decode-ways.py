# Decode Ways
# https://leetcode.com/problems/decode-ways/
# medium
#
# Tags: Aamzon, Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

def numDecodings(s: str) -> int:
    if not s: return 0

    dp = {}
    def solve(s):
        nonlocal dp

        if not s: return 1
        if s in dp: return dp[s]

        res = 0
        n = int(s[0])
        nn = int(s[:2]) if len(s) > 1 else None

        if n > 0:
            res += solve(s[1:])

            if nn and nn < 27:
                res += solve(s[2:])

        dp[s] = res
        return dp[s]

    return solve(s)

print(numDecodings("12"), 2)
print(numDecodings("226"), 3)
print(numDecodings(""), 1)

