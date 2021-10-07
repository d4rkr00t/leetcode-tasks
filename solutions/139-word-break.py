# Word Break
# https://leetcode.com/problems/word-break/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)

    def recur(cur, pos):
        if pos == len(s):
            return cur in wordSet

        cur += s[pos]

        return recur(
            cur, pos + 1) or (recur("", pos + 1) if cur in wordSet else False)

    return recur("", 0)


print(wordBreak(s="leetcode", wordDict=["leet", "code"]), True)
print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]), True)
print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]),
      False)
