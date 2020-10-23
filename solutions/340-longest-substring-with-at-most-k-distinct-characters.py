# Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# hard
#
# Tags: Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

from collections import Counter


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    c = Counter()
    ans = lo = 0
    for hi in range(len(s)):
        c[s[hi]] += 1

        while len(c.keys()) > k:
            ch = s[lo]
            c[ch] -= 1
            if c[ch] == 0:
                del c[ch]
            lo += 1

        ans = max(ans, hi - lo + 1)

    return ans


print(lengthOfLongestSubstringKDistinct("eceba", 2), 3)
print(lengthOfLongestSubstringKDistinct("ccaabbb", 2), 5)
print(lengthOfLongestSubstringKDistinct("aa", 1), 2)
