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
    res = lo = 0
    counter = collections.Counter()

    for hi, char in enumerate(s):
        counter[char] += 1

        while len(counter) > k:
            cc = s[lo]
            counter[cc] -= 1
            if counter[cc] == 0:
                del counter[cc]

            lo += 1

        res = max(res, hi - lo + 1)

    return res


print(lengthOfLongestSubstringKDistinct("eceba", 2), 3)
print(lengthOfLongestSubstringKDistinct("ccaabbb", 2), 5)
print(lengthOfLongestSubstringKDistinct("aa", 1), 2)
