# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(n^2)
# Space: O(1)
#
# Solution:
# TBD


def longestPalindrome(s: str) -> str:
    ans = ""
    pos = 0
    n = len(s)

    while pos < n:
        lo = hi = pos

        while hi + 1 < n and s[hi + 1] == s[lo]:
            hi += 1

        while lo >= 0 and hi < n and s[lo] == s[hi]:
            ans = s[lo:hi + 1] if len(ans) < hi - lo + 1 else ans

            lo -= 1
            hi += 1

        pos += 1

    return ans


print(longestPalindrome("babad"), "bab", "aba")
print(longestPalindrome("cbbd"), "bb")
