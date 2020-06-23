# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# easy
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

import collections

def firstUniqChar(s: str) -> int:
    ht = collections.Counter(s)

    for i,c in enumerate(s):
        if ht[c] == 1:
            return i

    return -1

print(firstUniqChar("leetcode"), 0)
print(firstUniqChar("loveleetcode"), 2)
