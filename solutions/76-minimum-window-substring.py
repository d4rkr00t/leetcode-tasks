# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# hard
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def minWindow(s: str, t: str) -> str:
    tc = collections.Counter(t)
    sc = collections.Counter()
    formed = 0
    required = len(tc)
    lo = 0
    ans = ""

    for i, c in enumerate(s):
        sc[c] += 1

        if sc[c] == tc[c]:
            formed += 1

        while lo <= i and formed == required:
            char = s[lo]

            if i - lo + 1 < len(ans) or not ans:
                ans = s[lo:i+1]

            sc[char] -= 1
            lo += 1

            if char in tc and sc[char] < tc[char]:
                formed -= 1

    return ans


print(minWindow("ADOBECODEBANC", "ABC"), "BANC")
