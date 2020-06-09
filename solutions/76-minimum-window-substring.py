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
# HashTable + TwoPointers

from collections import Counter

def minWindow(s: str, t: str) -> str:
    tt = Counter(t)

    def comp(tt, ts):
        for c in tt:
            if c not in ts or ts[c] < tt[c]:
                return False

        return True

    i = j = 0
    ans = None
    ts = Counter()
    while i <= j and j < len(s):
        char = s[j]
        if char in tt:
            ts[char] += 1

        while comp(tt, ts):
            ans = s[i:j+1] if not ans or 1 + j - i < len(ans) else ans
            char = s[i]
            ts[char] -= 1
            if ts[char] <= 0:
                del ts[char]

            i += 1

        j += 1

    return ans if ans else ""

print(minWindow("ADOBECODEBANC", "ABC"), "BANC")
