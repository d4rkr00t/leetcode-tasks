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

from typing import List
import collections


def removeStones(stones: List[List[int]]) -> int:
    graph = collections.defaultdict(list)

    for i, x in enumerate(stones):
        for j in range(i):
            y = stones[j]
            if x[0] == y[0] or x[1] == y[1]:
                graph[i].append(j)
                graph[j].append(i)

    N = len(stones)
    ans = 0

    seen = [False] * N

    for i in range(N):
        if not seen[i]:
            stack = [i]
            seen[i] = True
            while stack:
                ans += 1
                node = stack.pop()
                for nei in graph[node]:
                    if not seen[nei]:
                        stack.append(nei)
                        seen[nei] = True

            ans -= 1

    return ans


print(removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]), 3)
print(removeStones([[0, 0]]), 0)