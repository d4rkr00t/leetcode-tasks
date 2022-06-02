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
    if len(s) < len(t):
        return ""

    sCounter = collections.Counter()
    tCounter = collections.Counter(t)
    lo = 0
    ans = s

    def contains(sc, tc):
        for ch in tc.keys():
            if sc[ch] < tc[ch]:
                return False

        return True

    for hi, ch in enumerate(s):
        sCounter[ch] += 1

        while contains(sCounter, tCounter):
            if len(ans) > hi - lo + 1:
                ans = s[lo:hi + 1]
            sCounter[s[lo]] -= 1
            lo += 1

    return ans


print(minWindow("ADOBECODEBANC", "ABC"), "BANC")
