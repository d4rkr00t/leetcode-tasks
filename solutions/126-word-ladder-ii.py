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
import collections


def findLadders(beginWord: str, endWord: str,
                wordList: List[str]) -> List[List[str]]:
    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = collections.defaultdict(list)
        for w in layer:
            if w == endWord:
                res.extend(k for k in layer[w])
            else:
                for i in range(len(w)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        neww = w[:i] + c + w[i + 1:]
                        if neww in wordList:
                            newlayer[neww] += [j + [neww] for j in layer[w]]
        wordList -= set(newlayer.keys())
        layer = newlayer

    return res


print(
    findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
    [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]])

print(findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), [])
