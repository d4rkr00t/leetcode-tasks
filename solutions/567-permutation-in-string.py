# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# medium
#
# Tags: Facebook, Microsoft, Google
#
# Time:  O(s2)
# Space: O(s1)
#
# Solution:
# Two Pointers + Hash Map

import collections

def checkInclusion(s1: str, s2: str) -> bool:
    s1 = collections.Counter(s1)
    count = collections.Counter()

    j = 0
    for i, c in enumerate(s2):
        if c in s1:
            count[c] += 1
            if count == s1:
                return True

            while count[c] > s1[c]:
                if s2[j] in count:
                    count[s2[j]] -= 1
                j += 1

        else:
            count = collections.Counter()
            j = i

    return False

print(checkInclusion(s1 = "ab", s2 = "eidbaooo"), True)
print(checkInclusion(s1 = "ab", s2 = "eidboaooo"), False)
