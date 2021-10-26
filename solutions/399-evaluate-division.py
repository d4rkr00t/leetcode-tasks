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
import collections


def calcEquation(equations: List[List[str]], values: List[float],
                 queries: List[List[str]]) -> List[float]:
    graph = collections.defaultdict(list)
    ans = []

    def dfs(f, t, visited):
        if f not in graph or t not in graph:
            return -1.0

        if f == t:
            return 1.0

        visited.add(f)

        for nei, rel in graph[f]:
            if nei not in visited:
                res = dfs(nei, t, visited)
                if res != -1.0:
                    return res * rel

        return -1.0

    for i, [f, t] in enumerate(equations):
        val = values[i]
        graph[f].append((t, val))
        graph[t].append((f, 1 / val))

    for f, t in queries:
        ans.append(dfs(f, t, set()))

    return ans


print(
    calcEquation(equations=[["a", "b"], ["b", "c"]],
                 values=[2.0, 3.0],
                 queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"],
                          ["x", "x"]]), [6.0, 0.5, -1.0, 1.0, -1.0])
