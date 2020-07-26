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
    counter = collections.Counter()
    i = 0
    ans = 0

    for j, c in enumerate(s):
        counter[c] += 1

        while len(counter.keys()) > 2:
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                del counter[s[i]]

            i += 1

        ans = max(ans, j - i + 1)

    return ans


print(lengthOfLongestSubstringTwoDistinct("eceba"), 3)
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"), 5)
