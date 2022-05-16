# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def longestPalindrome(s: str) -> str:
    ans = ""

    def expand(lo, hi):
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1

        return s[lo + 1:hi]

    for i in range(len(s)):
        tmp = expand(i, i)
        if len(tmp) > len(ans):
            ans = tmp

        tmp = expand(i, i + 1)
        if len(tmp) > len(ans):
            ans = tmp

    return ans


print(longestPalindrome("babad"), "bab", "aba")
print(longestPalindrome("cbbd"), "bb")
