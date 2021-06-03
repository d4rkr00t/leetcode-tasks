# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# medium
#
# Tags: Google, Facebook, Amazon, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

import collections


def lengthOfLongestSubstring(s: str) -> int:
    cc = collections.Counter()
    ans = lo = 0

    for hi, ch in enumerate(s):
        cc[ch] += 1

        while cc[ch] > 1:
            cc[s[lo]] = max(cc[s[lo]] - 1, 0)
            lo += 1

        ans = max(ans, hi - lo + 1)

    return ans


print(lengthOfLongestSubstring("abcabcbb"), 3)
print(lengthOfLongestSubstring("bbbbb"), 1)
print(lengthOfLongestSubstring("pwwkew"), 3)
