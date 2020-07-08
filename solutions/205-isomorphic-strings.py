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
    s_ids = {}
    t_ids = {}
    s_i = t_i = 0

    for sc, tc in zip(s, t):
        if sc not in s_ids:
            s_ids[sc] = s_i
            s_i += 1

        if tc not in t_ids:
            t_ids[tc] = t_i
            t_i += 1

        if s_ids[sc] != t_ids[tc]:
            return False

    return True


print(isIsomorphic(s="egg", t="add"), True)
print(isIsomorphic(s="foo", t="bar"), False)
print(isIsomorphic(s="paper", t="title"), True)
