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

import collections


def firstUniqChar(s: str) -> int:
    counter = collections.Counter(s)

    for i, ch in enumerate(s):
        if counter[ch] == 1:
            return i

    return -1


print(firstUniqChar("leetcode"), 0)
print(firstUniqChar("loveleetcode"), 2)
