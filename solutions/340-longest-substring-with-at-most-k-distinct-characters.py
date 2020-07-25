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
    counter = collections.Counter()
    j = 0
    ans = 0

    for i, c in enumerate(s):
        counter[c] += 1

        while len(counter.keys()) > k:
            counter[s[j]] -= 1
            if counter[s[j]] == 0:
                del counter[s[j]]

            j += 1

        ans = max(ans, i-j+1)

    return ans


print(lengthOfLongestSubstringKDistinct("eceba", 2), 3)
print(lengthOfLongestSubstringKDistinct("ccaabbb", 2), 5)
print(lengthOfLongestSubstringKDistinct("aa", 1), 2)
