# Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# hard
#
# Tags: Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    count = collections.Counter()
    ans = lo = 0
    for hi, ch in enumerate(s):
        count[ch] += 1

        while len(count) > k:
            count[s[lo]] -= 1
            if count[s[lo]] == 0:
                del count[s[lo]]
            lo += 1

        ans = max(ans, hi - lo + 1)

    return ans


print(lengthOfLongestSubstringKDistinct("eceba", 2), 3)
print(lengthOfLongestSubstringKDistinct("ccaabbb", 2), 5)
print(lengthOfLongestSubstringKDistinct("aa", 1), 2)
