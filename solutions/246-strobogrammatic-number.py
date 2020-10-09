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
    table = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    lo = 0
    hi = len(num) - 1

    while lo <= hi:
        n_lo = num[lo]
        n_hi = table.get(num[hi], "")

        if n_lo != n_hi:
            return False

        lo += 1
        hi -= 1

    return True


print(isStrobogrammatic("69"), True)
print(isStrobogrammatic("88"), True)
print(isStrobogrammatic("962"), False)
