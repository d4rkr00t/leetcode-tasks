# Most Stones Removed with Same Row or Column
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import defaultdict
from typing import List


def removeStones(stones: List[List[int]]) -> int:
    graph = defaultdict(list)

    for i in range(len(stones)):
        for j in range(i + 1, len(stones)):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                graph[i].append(j)
                graph[j].append(i)

    visited = set()

    def dfs(node):
        count = 1
        visited.add(node)

        while graph[node]:
            nei = graph[node].pop()
            if nei not in visited:
                count += dfs(nei)

        return count

    ans = 0
    for i in range(len(stones)):
        if i not in visited:
            ans += dfs(i) - 1

    return ans


print(removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]), 3)
print(removeStones([[0, 0]]), 0)
