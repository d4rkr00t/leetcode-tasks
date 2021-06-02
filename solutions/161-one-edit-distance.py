# One Edit Distance
# https://leetcode.com/problems/one-edit-distance/
# medium
#
# Tags: Amazon
#
# Time:  O(n)
# Space: O(n)


def isOneEditDistance(s: str, t: str) -> bool:
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
print(isOneEditDistance(s="a", t=""), True)
print(isOneEditDistance(s="aa", t=""), False)
print(isOneEditDistance(s="aaa", t="aaba"), True)
print(isOneEditDistance(s="a", t="ac"), True)

# a b
# a c b

# 1 2 0 3
# 1 2 1 3
