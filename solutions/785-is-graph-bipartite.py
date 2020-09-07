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
    color = [0] * len(graph)

    def dfs(node, c):
        color[node] = c
        n_c = 2 if c == 1 else 1

        for nei in graph[node]:
            if color[nei] == c:
                return False
            if color[nei] == 0:
                res = dfs(nei, n_c)
                if not res:
                    return False

        return True

    for i in range(len(graph)):
        if color[i] == 0:
            res = dfs(i, 1)
            if not res:
                return False

    return True


print(isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]), True)
print(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]), False)
