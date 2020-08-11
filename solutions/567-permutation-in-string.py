# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# medium
#
# Tags: Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def checkInclusion(s1: str, s2: str) -> bool:
    s1c = collections.Counter(s1)
    s2c = collections.Counter()
    j = 0

    for i, c in enumerate(s2):
        if c in s1c:
            s2c[c] += 1

        while (i - j) + 1 > len(s1):
            ch = s2[j]
            j += 1
            s2c[ch] -= 1
            if s2c[ch] <= 0:
                del s2c[ch]

        if s2c == s1c:
            return True

    return False


print(checkInclusion(s1="ab", s2="eidbaooo"), True)
print(checkInclusion(s1="ab", s2="eidboaooo"), False)
