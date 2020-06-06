# Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# hard
#
# Tags: Facebook, Microsoft, Google
#
# Time:  O(n)
# Space: O(k)
#
# Solution:
# TBD

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    chars = {}
    j = ans = count = 0

    for i, c in enumerate(s):
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
            count += 1

            while count > k:
                chars[s[j]] -= 1
                if chars[s[j]] == 0:
                    del chars[s[j]]
                    count -= 1
                j += 1

        ans = max(ans, 1+i-j)

    return ans


print(lengthOfLongestSubstringKDistinct("eceba", 2), 3)
print(lengthOfLongestSubstringKDistinct("ccaabbb", 2), 5)
print(lengthOfLongestSubstringKDistinct("aa", 1), 2)
