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
    jj = set(J)
    count = 0

    for ch in S:
        if ch in jj:
            count += 1

    return count


print(numJewelsInStones(J="aA", S="aAAbbbb"), 3)
print(numJewelsInStones(J="z", S="ZZ"), 0)
