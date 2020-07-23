# Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/
# easy
#
# Tags: Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isStrobogrammatic(num: str) -> bool:
    pairs = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    i = 0
    j = len(num) - 1
    while i <= j:
        n1 = num[i]
        n2 = pairs.get(num[j], "")

        if n1 != n2:
            return False

        i += 1
        j -= 1

    return True


print(isStrobogrammatic("69"), True)
print(isStrobogrammatic("88"), True)
print(isStrobogrammatic("962"), False)
