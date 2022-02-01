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
    return sorted(s) == sorted(t)


print(isAnagram(s="anagram", t="nagaram"), True)
print(isAnagram(s="rat", t="car"), False)
