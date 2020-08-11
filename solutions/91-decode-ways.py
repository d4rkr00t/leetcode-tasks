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

    def recurse(pos):
        if pos in cache:
            return cache[pos]

        if pos == len(s):
            return 1

        n = int(s[pos])

        res = 0
        if n == 0:
            return res

        res += recurse(pos + 1)

        if pos + 1 < len(s):
            nn = n * 10 + int(s[pos+1])
            if nn <= 26 and nn > 0:
                res += recurse(pos + 2)

        cache[pos] = res
        return res

    return recurse(0)


print(numDecodings("12"), 2)
print(numDecodings("226"), 3)
print(numDecodings("01"), 0)
