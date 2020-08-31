# One Edit Distance
# https://leetcode.com/problems/one-edit-distance/
# medium
#
# Tags: Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isOneEditDistance(s: str, t: str) -> bool:
    n = len(s)
    m = len(t)
    if (not s and not t) or abs(m - n) > 1 or s == t:
        return False

    i = 0
    while i < min(m, n):
        if s[i] != t[i]:
            return s[i:] == t[i+1:] or s[i+1:] == t[i:] or s[i+1:] == t[i+1:]

        i += 1

    return True


print(isOneEditDistance(s="ab", t="acb"), True)
print(isOneEditDistance(s="cab", t="ad"), False)
print(isOneEditDistance(s="1203", t="1213"), True)
