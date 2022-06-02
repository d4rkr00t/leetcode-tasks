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
        newStr = []
        id = 0
        table = {}

        for ch in s:
            if ch not in table:
                table[ch] = str(id)
                id += 1

            newStr.append(table[ch])

        return "".join(newStr)

    return transform(s) == transform(t)


print(isIsomorphic(s="egg", t="add"), True)
print(isIsomorphic(s="foo", t="bar"), False)
print(isIsomorphic(s="paper", t="title"), True)
