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

from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    graph = {}
    for w in wordList:
        for i in range(len(w)):
            key = w[:i] + "*" + w[i+1:]
            graph[key] = graph.get(key, [])
            graph[key].append(w)

    queue = [(beginWord, 1)]
    visited = set([beginWord])

    while queue:
        cur, dist = queue.pop(0)

        for i in range(len(cur)):
            key = cur[:i] + "*" + cur[i+1:]
            if key in graph:
                for nei in graph[key]:
                    if nei == endWord:
                        return dist + 1

                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))

    return 0


print(ladderLength("hit", "cog", [
      "hot", "dot", "dog", "lot", "log", "cog"]), 5)
print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
