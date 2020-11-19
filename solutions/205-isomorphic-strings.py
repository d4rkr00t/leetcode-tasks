# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# easy
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n+m)
#
# Solution:
# Hashmap


def isIsomorphic(s: str, t: str) -> bool:
    s_m = {}
    t_m = {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]

        c1i = s_m.setdefault(c1, i)
        c2i = t_m.setdefault(c2, i)

        if c1i != c2i:
            return False

    return True


print(isIsomorphic(s="egg", t="add"), True)
print(isIsomorphic(s="foo", t="bar"), False)
print(isIsomorphic(s="paper", t="title"), True)
