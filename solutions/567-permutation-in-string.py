# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# medium
#
# Tags: Facebook, Microsoft, Google
#
# Time:  O(n) – n len of s1, m len of s2
# Space: O(1)

from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    s1_c = Counter(s1)
    s2_c = Counter()
    lo = 0

    for hi, ch in enumerate(s2):
        s2_c[ch] += 1

        while (hi - lo + 1) > len(s1):
            ch_lo = s2[lo]
            s2_c[ch_lo] -= 1
            if s2_c[ch_lo] == 0:
                del s2_c[ch_lo]

            lo += 1

        if s1_c == s2_c:
            return True

    return False


print(checkInclusion(s1="ab", s2="eidbaooo"), True)
print(checkInclusion(s1="ab", s2="eidboaooo"), False)
