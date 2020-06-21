# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# medium
#
# Tags: Facebook, Google, Amazon, Microsoft
#
# Time:  O(s+p)
# Space: O(1)
#
# Solution:
# TBD

def findAnagrams(s: str, p: str) -> [int]:
    pattern = [0] * 26
    match = [0] * 26
    ans = []

    for c in p:
        pattern[ord(c) - ord("a")] += 1

    j = None
    for i,c in enumerate(s):
        pos = ord(c) - ord("a")
        if pattern[pos] != 0:
            if j == None: j = i

            match[pos] += 1

            while match[pos] > pattern[pos] and j <= i:
                match[ord(s[j]) - ord("a")] -= 1
                j += 1

            if pattern == match:
                ans.append(j)

        else:
            match = [0] * 26
            j = None

    return ans


print(findAnagrams(s = "cbaebabacd", p = "abc"), [0, 6])
print(findAnagrams(s = "abab", p= "ab"), [0, 1, 2])
