# Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    colors = {}

    def dfs(node, color=0):
        colors[node] = color
        next_color = 1 if color == 0 else 0

        for nei in graph[node]:
            if nei in colors:
                if colors[nei] == color:
                    return False
                continue

            if not dfs(nei, next_color):
                return False

        return True

    for i in range(len(graph)):
        if i not in colors:
            if not dfs(i):
                return False

    return True


print(isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]), True)
print(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]), False)
