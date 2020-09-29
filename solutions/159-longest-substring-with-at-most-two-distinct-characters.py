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

from collections import Counter


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    lo = ans = 0
    counter = Counter()
    for hi, ch in enumerate(s):
        counter[ch] += 1

        while len(counter.keys()) > 2:
            lo_ch = s[lo]
            counter[lo_ch] -= 1

            if counter[lo_ch] <= 0:
                del counter[lo_ch]

            lo += 1

        ans = max(ans, hi - lo + 1)

    return ans


print(lengthOfLongestSubstringTwoDistinct("eceba"), 3)
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"), 5)
