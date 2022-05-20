# Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# easy
#
# Tags: Amazon, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def isAnagram(s: str, t: str) -> bool:
    s = "".join(sorted(list(s)))
    t = "".join(sorted(list(t)))
    return s == t


print(isAnagram(s="anagram", t="nagaram"), True)
print(isAnagram(s="rat", t="car"), False)
