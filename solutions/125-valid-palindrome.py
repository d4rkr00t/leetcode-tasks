# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# easy
#
# Tags: Facebook, Microsoft, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isPalindrome(s: str) -> bool:
    lo = 0
    hi = len(s) - 1

    while lo < hi:
        if not s[lo].isalnum():
            lo += 1
            continue

        if not s[hi].isalnum():
            hi -= 1
            continue

        if s[lo].lower() != s[hi].lower():
            return False

        lo += 1
        hi -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"), True)
print(isPalindrome("race a car"), False)
