# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def findAnagrams(s: str, p: str) -> [int]:
    pattern = collections.Counter(p)
    current = collections.Counter()
    pos = 0
    ans = []

    for i, c in enumerate(s):
        if c not in pattern:
            pos = i + 1
            current = collections.Counter()
            continue

        current[c] += 1
        while current[c] > pattern[c]:
            current[s[pos]] -= 1
            pos += 1
            if current[s[pos]] == 0:
                del current[s[pos]]

        if current == pattern:
            ans.append(pos)

    return ans


print(findAnagrams(s="cbaebabacd", p="abc"), [0, 6])
print(findAnagrams(s="abab", p="ab"), [0, 1, 2])
