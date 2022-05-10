# Word Ladder
# https://leetcode.com/problems/word-ladder/
# medium
#
# Tags: Amazon, Google, Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import defaultdict, deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    graph = defaultdict(list)

    def transform(word, pos):
        return word[:pos] + "*" + word[pos + 1:]

    def getNeighbours(word):
        res = []
        for i in range(len(word)):
            res.append(transform(word, i))

        return res

    for word in wordList:
        for nei in getNeighbours(word):
            graph[nei].append(word)

    queue = deque([(beginWord, 1)])
    visited = set([beginWord])

    while queue:
        cur, dist = queue.popleft()
        if cur == endWord:
            return dist

        for nei in getNeighbours(cur):
            for child in graph[nei]:
                if child not in visited:
                    queue.append((child, dist + 1))
                    visited.add(child)

    return 0


print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
      5)
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
