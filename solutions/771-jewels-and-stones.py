# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# easy
#
# Tags: Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def numJewelsInStones(J: str, S: str) -> int:
    jewels = set(J)
    ans = 0

    for c in S:
        if c in jewels:
            ans += 1

    return ans


print(numJewelsInStones(J="aA", S="aAAbbbb"), 3)
print(numJewelsInStones(J="z", S="ZZ"), 0)
