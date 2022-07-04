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


def numJewelsInStones(jewels: str, stones: str) -> int:
    jset = set(jewels)
    ans = 0
    for ch in stones:
        if ch in jset:
            ans += 1

    return ans


print(numJewelsInStones(jewels="aA", stones="aAAbbbb"), 3)
print(numJewelsInStones(jewels="z", stones="ZZ"), 0)
