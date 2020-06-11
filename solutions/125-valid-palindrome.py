# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# easy
#
# Tags: Facebook, Microsoft, Amazon
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two Pointers

def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i <= j:
        if not s[i].isalnum():
            i += 1
            continue

        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"), True)
print(isPalindrome("race a car"), False)
print(isPalindrome(""), True)
