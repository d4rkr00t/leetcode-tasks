# Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# easy
#
# Tags: Facebook, Microsoft
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

def validPalindrome(s: str) -> bool:
    def is_pali(s):
        return s == "".join(reversed(s))

    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            j = len(s) - i - 1
            return is_pali(s[i+1:j+1]) or is_pali(s[i:j])

    return True

print(validPalindrome("aba"), True)
print(validPalindrome("abca"), True)
print(validPalindrome("abcda"), False)

#   |
# abca

# abcda
#   ||
