# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# medium
#
# Tags: Google, Facebook, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD
import collections

def lengthOfLongestSubstring(s: str) -> int:
    j = l = 0
    counter = collections.Counter()

    for i,c in enumerate(s):
        counter[c] += 1

        while counter[c] > 1:
            counter[s[j]] -= 1
            j += 1

        l = max(l, i - j + 1)

    return l

print(lengthOfLongestSubstring("abcabcbb"), 3)
print(lengthOfLongestSubstring("bbbbb"), 1)
print(lengthOfLongestSubstring("pwwkew"), 3)
