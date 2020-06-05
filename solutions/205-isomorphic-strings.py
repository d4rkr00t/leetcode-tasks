# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# easy
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# two dicts

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    m1 = {}
    m2 = {}
    for i in range(len(s)):
        c_s = s[i]
        c_t = t[i]

        if c_s not in m1: m1[c_s] = i
        if c_t not in m2: m2[c_t] = i

        if m1[c_s] != m2[c_t]:
            return False

    return True

print(isIsomorphic(s = "egg", t = "add"), True)
print(isIsomorphic(s = "foo", t = "bar"), False)
print(isIsomorphic(s = "paper", t = "title"), True)
