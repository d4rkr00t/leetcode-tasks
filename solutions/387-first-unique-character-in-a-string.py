# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# easy
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(1) because of 26 letters
#
# Solution:
# TBD

import collections

def firstUniqChar(s: str) -> int:
    table = collections.Counter(s)

    for i,c in enumerate(s):
        if table[c] == 1:
            return i

    return -1


print(firstUniqChar("leetcode"), 0)
print(firstUniqChar("loveleetcode"), 2)
