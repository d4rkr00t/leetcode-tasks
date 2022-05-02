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

import collections
from gc import collect
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    ps = collections.Counter(p)
    ss = collections.Counter()
    lo = 0
    ans = []
    for hi, ch in enumerate(s):
        ss[ch] += 1

        if hi - lo + 1 > len(p):
            ss[s[lo]] -= 1
            if ss[s[lo]] == 0:
                del ss[s[lo]]
            lo += 1

        if ss == ps:
            ans.append(lo)

    return ans


print(findAnagrams(s="cbaebabacd", p="abc"), [0, 6])
print(findAnagrams(s="abab", p="ab"), [0, 1, 2])
