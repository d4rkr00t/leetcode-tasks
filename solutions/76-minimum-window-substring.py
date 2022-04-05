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

    def isMatch(c1, c2):
        for k, v in c1.items():
            if c2[k] < v: return False

        return True

    lo = 0
    ans = s
    for hi in range(len(s)):
        sc[s[hi]] += 1

        while isMatch(tc, sc):
            if hi - lo + 1 < len(ans):
                ans = s[lo:hi + 1]
            sc[s[lo]] -= 1
            if sc[s[lo]] <= 0:
                del sc[s[lo]]

            lo += 1

    return ans


print(minWindow("ADOBECODEBANC", "ABC"), "BANC")
