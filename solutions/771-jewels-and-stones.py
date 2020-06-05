# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# easy
#
# Tags: Amazon, Google
#
# Time:  O(S)
# Space: O(J)
#
# Solution:
# TBD

def numJewelsInStones(J: str, S: str) -> int:
    jewels = set(list(J))
    count = 0

    for c in S:
        if c in jewels:
            count += 1

    return count


print(numJewelsInStones(J = "aA", S = "aAAbbbb"), 3)
print(numJewelsInStones(J = "z", S = "ZZ"), 0)
