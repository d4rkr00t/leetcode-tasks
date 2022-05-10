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

from collections import defaultdict
from typing import List


def alienOrder(words: List[str]) -> str:
    graph = {}
    for w in words:
        for ch in w:
            graph[ch] = []

    cur = words[0]
    pos = 1
    while pos < len(words):
        tmp = words[pos]

        for ch1, ch2 in zip(cur, tmp):
            if ch1 != ch2:
                graph[ch1].append(ch2)
                break
        else:
            if len(cur) > len(tmp):
                return ""

        cur = tmp
        pos += 1

    visited = {}
    ans = []

    def dfs(ch):
        if ch in visited:
            if visited[ch] == 1:
                return False
            return True

        visited[ch] = 1
        for nei in graph[ch]:
            if not dfs(nei):
                return False

        ans.append(ch)
        visited[ch] = 2
        return True

    for ch in graph.keys():
        if not dfs(ch):
            return ""

    return "".join(ans[::-1])


print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")
print(alienOrder(["z", "x"]), "zx")
print(alienOrder(["z", "x", "z"]), "")
