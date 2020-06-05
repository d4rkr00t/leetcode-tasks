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
# Expand around center

def longestPalindrome(s: str) -> str:
    ans = ""

    def is_palindrome(s):
        return s == s[::-1]

    for i in range(len(s)):
        start = end = i

        while end < len(s) - 1 and s[end + 1] == s[start]:
            end += 1

        while start >= 0 and end <= len(s) and is_palindrome(s[start:end+1]):
            if 1 + end - start > len(ans):
                ans = s[start:end+1]
            end += 1
            start -= 1

    return ans

#                        | |
print(longestPalindrome("babad"), "bab", "aba")
print(longestPalindrome("cbbd"), "bb")
