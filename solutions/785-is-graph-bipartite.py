# Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  O(V+E)
# Space: O(V)
#
# Solution:
# BFS

from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    visited = [0] * n

    for i in range(n):
        if visited[i] != 0:
            continue

        queue = [i]
        visited[i] = 1

        while queue:
            cur = queue.pop(0)
            color = visited[cur]
            next_color = 2 if color == 1 else 1

            for nei in graph[cur]:
                if visited[nei] == color:
                    return False

                if visited[nei] == 0:
                    queue.append(nei)
                    visited[nei] = next_color

    return True


print(isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]), True)
print(isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]), False)
