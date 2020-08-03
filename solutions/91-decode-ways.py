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
    cache = {}

    def solve(pos):
        nonlocal cache
        if pos in cache:
            return cache[pos]

        if pos >= len(s):
            return 1

        cur = int(s[pos])

        if cur == 0:
            return 0

        ans = solve(pos + 1)
        if pos < len(s) - 1:
            cur = cur * 10 + int(s[pos+1])
            if cur <= 26:
                ans += solve(pos+2)

        cache[pos] = ans

        return ans

    return solve(0)


print(numDecodings("12"), 2)
print(numDecodings("226"), 3)
