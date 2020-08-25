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
    cache = {}

    def segment(offset):
        if offset in cache:
            return cache[offset]

        if offset == len(s):
            return True

        for w in wordDict:
            if s.startswith(w, offset) and segment(offset + len(w)):
                cache[offset] = True
                return True

        cache[offset] = False
        return False

    return segment(0)


print(wordBreak(s="leetcode", wordDict=["leet", "code"]), True)
print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]), True)
print(wordBreak(s="catsandog", wordDict=[
      "cats", "dog", "sand", "and", "cat"]), False)
