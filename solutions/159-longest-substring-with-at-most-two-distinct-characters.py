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
    cnt = collections.Counter()
    lo = ans = 0

    for hi, ch in enumerate(s):
        cnt[ch] += 1

        while len(cnt) > 2:
            loCh = s[lo]
            cnt[loCh] -= 1
            lo += 1
            if cnt[loCh] == 0:
                del cnt[loCh]

        ans = max(ans, hi - lo + 1)

    return ans


print(lengthOfLongestSubstringTwoDistinct("eceba"), 3)
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"), 5)
