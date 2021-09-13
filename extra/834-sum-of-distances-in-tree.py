# Sum of Distances in Tree
# https://leetcode.com/problems/sum-of-distances-in-tree/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import collections


def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    ans = [0] * n
    count = [1] * n
    graph = collections.defaultdict(set)

    for f, t in edges:
        graph[f].add(t)
        graph[t].add(f)

    def dfs(node=0, parent=None):
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

    def dfs2(node=0, parent=None):
        for child in graph[node]:
            if child != parent:
                ans[child] = ans[node] - count[child] + n - count[child]
                dfs2(child, node)

    dfs()
    dfs2()

    return ans


print(
    sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]),
    [8, 12, 6, 10, 10, 10])

print(sumOfDistancesInTree(n=1, edges=[]), [0])
print(sumOfDistancesInTree(n=2, edges=[[1, 0]]), [1, 1])
