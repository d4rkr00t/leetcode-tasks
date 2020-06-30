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
# BFS

def ladderLength(beginWord: str, endWord: str, wordList: [str]) -> int:
    graph = {}
    L = len(beginWord)

    for w in [beginWord] + wordList:
        for i in range(L+1):
            cur = w[:i] + "*" + w[i+1:]
            graph[cur] = graph.get(cur, [])
            graph[cur].append(w)

    queue = [(beginWord, 1)]
    seen = set([beginWord])

    while queue:
        w,d = queue.pop(0)

        for i in range(L+1):
            cur = w[:i] + "*" + w[i+1:]
            for w2 in graph[cur]:
                if w2 == endWord:
                    return d + 1
                if w2 not in seen:
                    queue.append((w2, d+1))
                    seen.add(w2)

    return 0

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]), 0)
