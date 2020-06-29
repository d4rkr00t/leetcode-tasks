# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# medium
#
# Tags: Facebook, Microsoft, Google
#
# Time:  O(n) – n = max(s1, s2)
# Space: O(1)
#
# Solution:
# TBD

import collections

def checkInclusion(s1: str, s2: str) -> bool:
    dict = collections.Counter()
    pattern = collections.Counter(s1)
    lo = 0

    for i in range(len(s2)):
        dict[s2[i]] += 1

        if i - lo < len(s1) - 1: continue

        if dict == pattern:
            return True

        dict[s2[lo]] -= 1
        if dict[s2[lo]] == 0:
            del dict[s2[lo]]

        lo += 1

    return False

print(checkInclusion(s1 = "ab", s2 = "eidbaooo"), True)
print(checkInclusion(s1 = "ab", s2 = "eidboaooo"), False)
