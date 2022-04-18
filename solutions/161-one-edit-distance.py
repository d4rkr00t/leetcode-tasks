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
    if s == t:
        return False

    if len(s) > len(t):
        return isOneEditDistance(t, s)

    for (i, ch) in enumerate(s):
        if ch == t[i]:
            continue

        return s == t[:i] + t[i + 1:] or s[:i] + s[i + 1:] == t[:i] + t[i + 1:]

    return len(t) - len(s) < 2


print(isOneEditDistance(s="ab", t="acb"), True)
print(isOneEditDistance(s="cab", t="ad"), False)
print(isOneEditDistance(s="1203", t="1213"), True)

# ad
# cad
#
# ca
# cad
#
# cad
# cab

# cad
# cxad
