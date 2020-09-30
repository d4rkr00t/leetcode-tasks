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
    def expand(s, p1, p2):
        if s[p1] != s[p2]:
            return s[p1]

        while True:
            if p1 - 1 < 0 or p2+1 == len(s):
                break

            if s[p1 - 1] != s[p2+1]:
                break

            p1 -= 1
            p2 += 1

        return s[p1:p2+1]

    ans = ""
    for i in range(len(s)):
        tmp = expand(s, i, i)
        tmp2 = expand(s, i, i+1) if i+1 < len(s) else ""
        tmp = tmp if len(tmp) > len(tmp2) else tmp2
        ans = tmp if len(tmp) > len(ans) else ans

    return ans


print(longestPalindrome("babad"), "bab", "aba")
print(longestPalindrome("cbbd"), "bb")
