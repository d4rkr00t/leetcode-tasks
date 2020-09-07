# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# easy
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import Counter


def firstUniqChar(s: str) -> int:
    counter = Counter(s)

    for i, c in enumerate(s):
        if counter[c] == 1:
            return i

    return -1


print(firstUniqChar("leetcode"), 0)
print(firstUniqChar("loveleetcode"), 2)
