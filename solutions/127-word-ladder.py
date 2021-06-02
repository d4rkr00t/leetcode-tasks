# Word Ladder
# https://leetcode.com/problems/word-ladder/
# medium
#
# Tags: Amazon, Google, Facebook, Microsoft
#
# Time:  O(N*W + E + V)
# Space: O(N*W + E + V)
#
# Solution:
# TBD

from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    graph = {}

    def transform(w, i):
        return w[:i] + "*" + w[i + 1:]

    for w in wordList:
        for i in range(len(w)):
            tWord = transform(w, i)
            if tWord not in graph:
                graph[tWord] = []
            graph[tWord].append(w)

    queue = [(beginWord, 1)]
    visited = set([beginWord])

    print(graph)

    while queue:
        cur, d = queue.pop(0)
        nei = []

        for i in range(len(cur)):
            tWord = transform(cur, i)
            if tWord not in graph:
                continue

            nei.extend(graph[tWord])

        for n in nei:
            if n not in visited:
                visited.add(n)
                if n == endWord:
                    return d + 1
                queue.append((n, d + 1))

    return 0


print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
      5)
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)

# {
#   "*ot": ["hot", "dot", "lot"],
#   "h*t": ["hot"],
#   "ho*": ["hot"],
#   "d*t": ["dot"],
#   "do*": ["dot", "dog"],
#   "*og": ["dog", "cog"]
# }
