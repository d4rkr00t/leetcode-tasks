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


def repeatedStringMatch(a: str, b: str) -> int:
    q = (len(b) - 1) // len(a) + 1
    for i in range(2):
        if b in a * (q+i):
            return q+i
    return -1


print(repeatedStringMatch(a="abcd", b="cdabcdab"), 3)
print(repeatedStringMatch(a="a", b="aa"), 2)
print(repeatedStringMatch(a="a", b="a"), 1)
print(repeatedStringMatch(a="abc", b="wxyz"), -1)
print(repeatedStringMatch(a="fabcde", b="abcd"), 1)

# cdabcdab
#   abcd
#
#  abcdabcd
# fabcde


# cdabcdab = 2 3 0 1 2 3 0 1
# abcd = 0 1 2 3
