# Evaluate Division
# https://leetcode.com/problems/evaluate-division/
# medium
#
# Tags: Google, Amazon, Facebook
#
# Time:  O(Q * (E+V)) – where Q = number of queries, E = number of edges, V = number of vertices
# Space: O(E+V)
#
# Solution:
# BFS

from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = {}

    for (f, t), v in zip(equations, values):
        graph[f] = graph.get(f, [])
        graph[t] = graph.get(t, [])
        graph[f].append((t, v))
        graph[t].append((f, 1/v))

    def bfs(f, t):
        if f not in graph or t not in graph:
            return -1.0

        if f == t:
            return 1.0

        queue = [(f, 1.0)]
        visited = set([f])

        while queue:
            cur, val = queue.pop(0)

            if cur == t:
                return val

            for nei, nei_val in graph[cur]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, val * nei_val))

        return -1.0

    ans = []

    for f, t, in queries:
        ans.append(bfs(f, t))

    return ans


print(calcEquation(
    equations=[["a", "b"], ["b", "c"]],
    values=[2.0, 3.0],
    queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
), [6.0, 0.5, -1.0, 1.0, -1.0])
