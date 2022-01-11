# Cracking the Safe
# https://leetcode.com/problems/cracking-the-safe/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import defaultdict
from itertools import product


def crackSafe(n: int, k: int) -> str:
    if n == 1:
        return ''.join(map(str, range(k)))

    graph = defaultdict(list)

    for comb in product(range(k), repeat=n):
        graph[comb[:-1]].append(comb[1:])

    path = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())
        path.append(node[0])

    dfs(tuple([0] * (n - 1)))

    return ''.join(map(str, [*reversed(path), *([0] * (n - 2))]))


print(crackSafe(n=1, k=2), "01")
print(crackSafe(n=2, k=2), "01100")
print(crackSafe(n=3, k=2), "01100")
