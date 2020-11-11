# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers

from typing import List
from collections import Counter


def findAnagrams(s: str, p: str) -> List[int]:
    p_c = Counter(p)
    s_c = Counter()
    lo = 0
    ans = []

    for hi, ch in enumerate(s):
        if ch not in p_c:
            s_c = Counter()
            lo = hi+1
            continue

        s_c[ch] += 1
        while s_c[ch] > p_c[ch]:
            lo_ch = s[lo]
            s_c[lo_ch] -= 1
            lo += 1
            if s_c[lo_ch] <= 0:
                del s_c[lo_ch]

        if s_c == p_c:
            ans.append(lo)

    return ans


print(findAnagrams(s="cbaebabacd", p="abc"), [0, 6])
print(findAnagrams(s="abab", p="ab"), [0, 1, 2])
