# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
# hard
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def alienOrder(words: List[str]) -> str:
    graph = {}

    for w in words:
        for ch in w:
            graph[ch] = graph.get(ch, set())

    prev_word = words[0]
    for i in range(1, len(words)):
        cur_word = words[i]

        for ch1, ch2 in zip(prev_word, cur_word):
            if ch1 != ch2:
                graph[ch2].add(ch1)
                break

        prev_word = cur_word

    def topSort(graph):
        ans = []
        visited = {}

        def dfs(node):
            visited[node] = 1

            for nei in graph[node]:
                if visited.get(nei, 0) == 1:
                    return False

                if nei not in visited:
                    if not dfs(nei):
                        return False

            visited[node] = 2
            ans.append(node)

            return True

        for key in graph.keys():
            if key not in visited:
                if not dfs(key):
                    return ""

        return "".join(ans)

    return topSort(graph)


print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")
print(alienOrder(["z", "x"]), "zx")
print(alienOrder(["z", "x", "z"]), "")
