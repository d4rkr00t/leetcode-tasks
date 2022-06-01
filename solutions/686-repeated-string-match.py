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

import math


def repeatedStringMatch(a: str, b: str) -> int:
    if a == b:
        return 1

    reps = math.ceil(len(b) / len(a)) + 1
    s = a * reps
    idx = s.find(b)

    if idx == -1:
        return -1

    return math.ceil((idx + len(b)) / len(a))


print(repeatedStringMatch(a="abcd", b="cdabcdab"), 3)
print(repeatedStringMatch(a="a", b="aa"), 2)
print(repeatedStringMatch(a="a", b="a"), 1)
print(repeatedStringMatch(a="abc", b="wxyz"), -1)
print(repeatedStringMatch(a="aabbb", b="bbaa"), 2)

# abcd = 4
# cdabcdab = 8
# reps = 8/4 + 1 = 3
# abcd + abcd + abcd
# abcdabcdabcd = 12
#   cdabcdab
#   2   +  8 = 10
# 10/4 = 2.5 = 3
#
