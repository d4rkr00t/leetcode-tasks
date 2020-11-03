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

from collections import Counter


def firstUniqChar(s: str) -> int:
    counter = Counter(s)

    for i, ch in enumerate(s):
        if counter[ch] == 1:
            return i


print(firstUniqChar("leetcode"), 0)
print(firstUniqChar("loveleetcode"), 2)
