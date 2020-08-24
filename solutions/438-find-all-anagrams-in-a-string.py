# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List

import collections


def findAnagrams(s: str, p: str) -> List[int]:
    p_c = collections.Counter(p)
    s_c = collections.Counter()
    ans = []
    lo = 0

    for hi, c in enumerate(s):
        if not c in p_c:
            s_c = collections.Counter()
            lo = hi + 1
            continue

        s_c[c] += 1

        while s_c[c] > p_c[c]:
            cc = s[lo]
            if cc in s_c:
                s_c[cc] -= 1

            if s_c[cc] == 0:
                del s_c[cc]

            lo += 1

        if s_c == p_c:
            ans.append(lo)

    return ans


print(findAnagrams(s="cbaebabacd", p="abc"), [0, 6])
print(findAnagrams(s="abab", p="ab"), [0, 1, 2])
