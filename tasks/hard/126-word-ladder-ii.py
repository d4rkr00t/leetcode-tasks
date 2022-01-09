# Word Ladder II
# https://leetcode.com/problems/word-ladder-ii/
# hard
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    pass


print(findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), [
    ["hit", "hot", "dot", "dog", "cog"],
    ["hit", "hot", "lot", "log", "cog"]
])

print(findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), [])
