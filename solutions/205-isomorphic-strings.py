# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# easy
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def isIsomorphic(s: str, t: str) -> bool:
    ch_map1 = {}
    ch_map2 = {}

    for ch1, ch2 in zip(s, t):
        if not ch1 in ch_map1: ch_map1[ch1] = ch2
        if not ch2 in ch_map2: ch_map2[ch2] = ch1

        if ch2 != ch_map1[ch1]: return False
        if ch1 != ch_map2[ch2]: return False

    return True


print(isIsomorphic(s="egg", t="add"), True)
print(isIsomorphic(s="foo", t="bar"), False)
print(isIsomorphic(s="paper", t="title"), True)
print(isIsomorphic(s="badc", t="baba"), False)
