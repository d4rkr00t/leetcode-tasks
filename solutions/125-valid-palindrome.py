# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# easy
#
# Tags: Facebook, Microsoft, Amazon
#
# Time:  O(n)
# Space: O(1)


def isPalindrome(s: str) -> bool:
    s = s.lower()
    lo = 0
    hi = len(s) - 1

    while lo <= hi:
        l_ch = s[lo]
        h_ch = s[hi]

        if not l_ch.isalnum():
            lo += 1
            continue

        if not h_ch.isalnum():
            hi -= 1
            continue

        if l_ch != h_ch:
            return False

        lo += 1
        hi -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"), True)
print(isPalindrome("race a car"), False)
