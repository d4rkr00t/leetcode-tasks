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
    def transform(s):
        char_map = {}
        i = 0
        res = ""

        for c in s:
            if not c in char_map:
                char_map[c] = str(i)
                i += 1

            res += char_map[c]

        return res

    return transform(s) == transform(t)


print(isIsomorphic(s="egg", t="add"), True)
print(isIsomorphic(s="foo", t="bar"), False)
print(isIsomorphic(s="paper", t="title"), True)
