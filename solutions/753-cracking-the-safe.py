# Cracking the Safe
# https://leetcode.com/problems/cracking-the-safe/
# hard
#
# Tags: Google
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
        return "".join([str(i) for i in range(k)])

    graph = defaultdict(list)
    for comb in product(range(k), repeat=n):
        graph[comb[:-1]].append(comb[1:])

    def dfs(node, path):
        while graph[node]:
            cur = graph[node].pop()
            dfs(cur, path)

        path.append(str(node[0]))

    path = []
    dfs(tuple([0] * (n - 1)), path)

    return "".join(path[::-1]) + ("0" * (n - 2))


# print(crackSafe(n=1, k=2), "01")
print(crackSafe(n=2, k=2), "01100")
print(crackSafe(n=3, k=2), "0011101000")

# 000 001 010 011 100 101 110 111

# 00 -> 01 -> 10
#          -> 11
