# Unique Length-3 Palindromic Subsequences
# https://leetcode.com/contest/weekly-contest-249/problems/unique-length-3-palindromic-subsequences/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def countPalindromicSubsequence(s: str) -> int:
    ans = set()
    seen = set()
    for lo in range(len(s)):
        if s[lo] in seen:
            continue

        hi = len(s) - 1
        while s[hi] != s[lo] and hi - lo > 1:
            hi -= 1

        if hi - lo > 1:
            for m in range(lo + 1, hi):
                temp = s[lo] + s[m] + s[hi]
                ans.add(temp)

        seen.add(s[lo])

    return len(ans)


print(countPalindromicSubsequence("aabca"), 3)
print(countPalindromicSubsequence("adc"), 0)
print(countPalindromicSubsequence("bbcbaba"), 4)

# a a b c a
# a a a
# a b a
# a c a
# 3 2 0 0 0
