# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# medium
#
# Tags: Google, Facebook, Amazon, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# HashSet

def lengthOfLongestSubstring(s: str) -> int:
    hs = set()
    ans = 0
    i = j = 0

    while i < len(s) and j < len(s):
        if not s[j] in hs:
            hs.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            hs.remove(s[i])
            i += 1

    return ans


print(lengthOfLongestSubstring("abcabcbb"), 3)
print(lengthOfLongestSubstring("abcabcdbb"), 4)
print(lengthOfLongestSubstring("bbbbb"), 1)
print(lengthOfLongestSubstring("pwwkew"), 3)
