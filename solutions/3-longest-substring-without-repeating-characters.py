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
    counter = collections.Counter()
    lo = ans = 0
    for hi, ch in enumerate(s):
        counter[ch] += 1

        while counter[ch] > 1:
            lo_ch = s[lo]
            counter[lo_ch] -= 1
            lo += 1

        ans = max(ans, hi - lo + 1)

    return ans


print(lengthOfLongestSubstring("abcabcbb"), 3)
print(lengthOfLongestSubstring("bbbbb"), 1)
print(lengthOfLongestSubstring("pwwkew"), 3)
