# Evaluate Division
# https://leetcode.com/problems/evaluate-division/
# medium
#
# Tags: Google, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = {}

    # Build a graph
    for i, (f, t) in enumerate(equations):
        graph[f] = graph.get(f, [])
        graph[t] = graph.get(t, [])

        graph[f].append((t, values[i]))
        graph[t].append((f, 1/values[i]))

    # BFS queries
    ans = []

    def bfs(start, end):
        queue = [(start, 1.0)]
        visited = set([start])

        while queue:
            cur, cur_cost = queue.pop(0)
            if not cur in graph:
                continue

            for to, cost in graph[cur]:
                if to == end:
                    return cost * cur_cost

                if to not in visited:
                    visited.add(to)
                    queue.append((to, cur_cost * cost))

        return -1.0

    for start, end in queries:
        ans.append(bfs(start, end))

    return ans


print(calcEquation(
    equations=[["a", "b"], ["b", "c"]],
    values=[2.0, 3.0],
    queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
), [6.0, 0.5, -1.0, 1.0, -1.0])
