# Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# medium
#
# Tags: Microsoft, Google, Facebook
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers

def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    chars = {}
    uniq = start = ans = 0

    for i, c in enumerate(s):
        if c in chars:
            chars[c] += 1
        else:
            uniq += 1
            chars[c] = 1

            while uniq > 2:
                c = s[start]
                chars[c] -= 1
                start += 1

                if chars[c] == 0:
                    uniq -= 1
                    del chars[c]

        ans = max(ans, (i + 1) - start)

    return ans

print(lengthOfLongestSubstringTwoDistinct("eceba"), 3)
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"), 5)
