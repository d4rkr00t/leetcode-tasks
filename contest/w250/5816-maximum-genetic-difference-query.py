# Maximum Genetic Difference Query
# https://leetcode.com/problems/maximum-genetic-difference-query/
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
from collections import defaultdict


class Trie:
    def __init__(self):
        self.root = {-1: 0}

    def insert(self, num, f):
        d = self.root
        for i in range(18, -1, -1):
            bit = (num >> i) & 1
            d = d.setdefault(bit, dict())
            d[-1] = d.get(-1, 0) + f

    def find(self, num):
        node = self.root
        res = 0
        for i in range(18, -1, -1):
            bit = (num >> i) & 1
            desired = 1 - bit if 1 - bit in node and node[1 -
                                                          bit][-1] > 0 else bit
            res += (desired ^ bit) << i
            node = node[desired]
        return res


def maxGeneticDifference(parents, queries):
    Q, graph = defaultdict(list), defaultdict(list)
    for i, (node, val) in enumerate(queries):
        Q[node].append((i, val))

    for i, x in enumerate(parents):
        graph[x].append(i)

    ans, trie = [-1 for _ in queries], Trie()

    def dfs(node):
        trie.insert(node, 1)
        for i, val in Q[node]:
            ans[i] = trie.find(val)
        for neib in graph[node]:
            dfs(neib)
        trie.insert(node, -1)

    dfs(graph[-1][0])
    return ans


print(
    maxGeneticDifference(parents=[-1, 0, 1, 1],
                         queries=[[0, 2], [3, 2], [2, 5]]), [2, 3, 7])

print(
    maxGeneticDifference(parents=[3, 7, -1, 2, 0, 7, 0, 2],
                         queries=[[4, 6], [1, 15], [0, 5]]), [6, 14, 7])
