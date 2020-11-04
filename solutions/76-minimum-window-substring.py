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

from collections import Counter


def minWindow(s: str, t: str) -> str:
    t_c = Counter(t)
    s_c = Counter()
    lo, ans = 0, s*2

    def match(c1, c2):
        for k in c1.keys():
            if not k in c2 or c1[k] > c2[k]:
                return False

        return True

    for hi, ch in enumerate(s):
        if ch in t_c:
            s_c[ch] += 1

        while match(t_c, s_c):
            if len(ans) > hi-lo + 1:
                ans = s[lo:hi+1]

            lo_ch = s[lo]
            if lo_ch in s_c:
                s_c[lo_ch] -= 1

                if s_c[lo_ch] == 0:
                    del s_c[lo_ch]

            lo += 1

    return ans if ans != s * 2 else ""


print(minWindow("ADOBECODEBANC", "ABC"), "BANC")
