# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# medium
#
# Tags: Facebook, Microsoft, Google
#
# Time:  O(s1+s2)
# Space: O(s1+s2)
#
# Solution:
# TBD

import collections


def checkInclusion(s1: str, s2: str) -> bool:
    cs1 = collections.Counter(s1)
    cs2 = collections.Counter()
    lo = 0

    for ch in s2:
        if ch not in s2:
            cs2 = collections.Counter()
            continue

        cs2[ch] += 1
        while cs2[ch] > cs1[ch]:
            cs2[s2[lo]] -= 1
            if cs2[s2[lo]] == 0:
                del cs2[s2[lo]]
            lo += 1

        if cs1 == cs2:
            return True

    return False


print(checkInclusion(s1="ab", s2="eidbaooo"), True)
print(checkInclusion(s1="ab", s2="eidboaooo"), False)
print(checkInclusion(s1="adc", s2="bcda"), True)
