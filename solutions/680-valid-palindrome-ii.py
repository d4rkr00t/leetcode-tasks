# Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# easy
#
# Tags: Facebook, Microsoft
#
# Time:  O(N)
# Space: O(1)

def validPalindrome(s: str) -> bool:
    def is_pali_range(i, j):
        return s[i:j+1] == s[i:j+1][::-1]

    for i in range(len(s)//2):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            return is_pali_range(i+1, j) or is_pali_range(i, j-1)

    return True


print(validPalindrome("aba"), True)
print(validPalindrome("abca"), True)
print(validPalindrome("abcda"), False)
