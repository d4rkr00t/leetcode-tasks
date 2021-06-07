# Repeated String Match
# https://leetcode.com/problems/repeated-string-match/
# medium
#
# Tags: Google, Facebook, Amazon
#
# Time:  O(n*a)
# Space: O(1)
#
# Solution:
# TBD


def repeatedStringMatch(a: str, b: str) -> int:
    times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
    for i in range(2):
        if B in (A * (times + i)):
        return times + i
    return -1


print(repeatedStringMatch(a="abcd", b="cdabcdab"), 3)
print(repeatedStringMatch(a="a", b="aa"), 2)
print(repeatedStringMatch(a="a", b="a"), 1)
print(repeatedStringMatch(a="ba", b="a"), 1)
print(repeatedStringMatch(a="abc", b="wxyz"), -1)
