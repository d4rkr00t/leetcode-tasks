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

    def expand(i, j):
        nonlocal ans
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break

            if len(ans) < (j - i) + 1:
                ans = s[i:j + 1]
            i -= 1
            j += 1

    for i in range(len(s)):
        expand(i, i)
        if i < len(s) - 1:
            expand(i, i + 1)

    return ans


print(longestPalindrome("babad"), "bab", "aba")
print(longestPalindrome("cbbd"), "bb")
print(longestPalindrome("aaaaab"), "aaaaa")
