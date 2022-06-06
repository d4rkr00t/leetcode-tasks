# Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# easy
#
# Tags: Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def validPalindrome(s: str) -> bool:
    lo = 0
    hi = len(s) - 1

    def isPalindrome(s):
        return s == "".join(reversed(s))

    while lo <= hi:
        if s[lo] != s[hi]:
            return isPalindrome(s[:lo] +
                                s[lo + 1:]) or isPalindrome(s[:hi] +
                                                            s[hi + 1:])

        lo += 1
        hi -= 1

    return True


print(validPalindrome("aba"), True)
print(validPalindrome("abca"), True)
print(validPalindrome("abcda"), False)
