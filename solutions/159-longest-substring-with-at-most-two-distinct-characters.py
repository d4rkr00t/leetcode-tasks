# Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# medium
#
# Tags: Microsoft, Google, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    count = collections.Counter()

    lo = ans = 0
    for hi, ch in enumerate(s):
        count[ch] += 1
        while len(count) > 2:
            lo_ch = s[lo]
            count[lo_ch] -= 1
            if count[lo_ch] == 0:
                del count[lo_ch]

            lo += 1

        ans = max(ans, hi - lo + 1)

    return ans


print(lengthOfLongestSubstringTwoDistinct("eceba"), 3)
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"), 5)
