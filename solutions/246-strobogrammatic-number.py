# Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/
# easy
#
# Tags: Facebook, Google
#
# Time:  O(n)
# Space: O(1)

from math import ceil


def isStrobogrammatic(num: str) -> bool:
    table = {"6": "9", "9": "6", "0": "0", "1": "1", "8": "8"}

    for i in range(ceil(len(num) / 2)):
        c1 = num[i]
        c2 = num[~i]

        if not c1 in table or not c2 in table:
            return False

        if c1 != table.get(c2, c2):
            return False

    return True


print(isStrobogrammatic("69"), True)
print(isStrobogrammatic("88"), True)
print(isStrobogrammatic("962"), False)
print(isStrobogrammatic("010"), True)
print(isStrobogrammatic("0"), True)
