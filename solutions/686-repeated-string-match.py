# Repeated String Match
# https://leetcode.com/problems/repeated-string-match/
# medium
#
# Tags: Google, Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from math import ceil


def repeatedStringMatch(a: str, b: str) -> int:
    times = ceil(len(b) / len(a))

    for i in range(2):
        if b in (a * (times + i)):
            return times + i

    return -1


print(repeatedStringMatch(a="abcd", b="cdabcdab"), 3)
print(repeatedStringMatch(a="a", b="aa"), 2)
print(repeatedStringMatch(a="a", b="a"), 1)
print(repeatedStringMatch(a="abc", b="wxyz"), -1)

# cdabcdab cdabcdab
#   abcdab cdabcd
#
# aa aa aa
# aa aa aa
