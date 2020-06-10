# Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/
# easy
#
# Tags: Facebook, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

def isStrobogrammatic(num: str) -> bool:
    pairs = { "0": "0", "1": "1", "6": "9", "8": "8", "9": "6" }

    reverse = ""

    for c in num:
        if not c in pairs: return False
        reverse = pairs[c] + reverse

    return reverse == num

print(isStrobogrammatic("69"), True)
print(isStrobogrammatic("88"), True)
print(isStrobogrammatic("962"), False)
