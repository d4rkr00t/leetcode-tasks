# Word Break
# https://leetcode.com/problems/word-break/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  O(n^2)
# Space: O(n)
#
# Solution:
# Recursion + Cache

from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    cache = [None] * len(s)
    n = len(s)

    def recur(offset):
        if offset == n:
            return True

        if cache[offset] != None:
            return cache[offset]

        for word in wordDict:
            if s.startswith(word, offset):
                res = recur(offset + len(word))
                if res:
                    cache[offset] = True
                    return True

        cache[offset] = False
        return False

    return recur(0)


print(wordBreak(s="leetcode", wordDict=["leet", "code"]), True)
print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]), True)
print(wordBreak(s="catsandog", wordDict=[
      "cats", "dog", "sand", "and", "cat"]), False)
