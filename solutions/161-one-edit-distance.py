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
    if not s and not t or s == t:
        return False

    if abs(len(s) - len(t)) > 1:
        return False

    if len(s) > len(t):
        return isOneEditDistance(t, s)

    t_p = 0
    s_p = 0
    dist = 0
    while s_p < len(s) and t_p < len(t):
        t_c = t[t_p]
        s_c = s[s_p]

        if t_c != s_c:
            dist += 1
            if len(t) == len(s):
                t_p += 1
                s_p += 1
            else:
                t_p += 1
        else:
            t_p += 1
            s_p += 1

    return True if dist <= 1 else False


print(isOneEditDistance(s="dacb", t="acb"), True)
print(isOneEditDistance(s="ab", t="acb"), True)
print(isOneEditDistance(s="cab", t="ad"), False)
print(isOneEditDistance(s="1203", t="1213"), True)

# acb
# dacb
