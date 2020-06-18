# Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s

    first_match = bool(s) and p[0] in (s[0], ".")

    if len(p) >= 2 and p[1] == "*":
        return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
    else:
        return first_match and self.isMatch(s[1:], p[1:])


print(isMatch("aa", "a"), False)
print(isMatch("aa", "a*"), True)
print(isMatch("ab", ".*"), True)
print(isMatch("aab", "c*a*b"), True)
print(isMatch("mississippi", "mis*is*p*."), False)
#                  |              |
