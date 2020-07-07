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
    l = ""

    def find_palindrome(lo, hi):
        nonlocal l

        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1

        if hi - lo - 1 > len(l):
            l = s[lo+1:hi]

    for i in range(len(s)):
        find_palindrome(i, i)
        find_palindrome(i, i+1)

    return l


print(longestPalindrome("babad"), "bab", "aba")
print(longestPalindrome("cbbd"), "bb")
