# The Most Similar Path in a Graph
# https://leetcode.com/problems/the-most-similar-path-in-a-graph/
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


def mostSimilar(n: int, roads: List[List[int]], names: List[str],
                targetPath: List[str]) -> List[int]:

    graph = defaultdict(set)
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    dp = defaultdict(lambda: float("inf"))
    back = defaultdict(lambda: "")
    L = len(targetPath)

    for i in range(L):
        for j in range(n):
            for nei in graph[j]:
                cur = (dp[i - 1, nei]
                       if i else 0) + (0 if targetPath[i] == names[j] else 1)

                if cur < dp[i, j]:
                    dp[i, j] = cur
                    back[i, j] = nei

    min_dist = min(dp[L - 1, j] for j in range(n))
    pick_last = -1

    for j in range(n):
        if dp[L - 1, j] == min_dist:
            pick_last = j
            break

    cur = pick_last
    i = L - 1
    ans = []
    while i >= 0:
        ans.append(cur)
        cur = back[i, cur]
        i -= 1

    ans = ans[::-1]

    return ans


print(
    mostSimilar(n=5,
                roads=[[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
                names=["ATL", "PEK", "LAX", "DXB", "HND"],
                targetPath=["ATL", "DXB", "HND", "LAX"]), [0, 2, 4, 2])

print(
    mostSimilar(
        n=4,
        roads=[[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],
        names=["ATL", "PEK", "LAX", "DXB"],
        targetPath=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX"]),
    [0, 1, 0, 1, 0, 1, 0, 1])

print(
    mostSimilar(n=6,
                roads=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
                names=["ATL", "PEK", "LAX", "ATL", "DXB", "HND"],
                targetPath=["ATL", "DXB", "HND", "DXB", "ATL", "LAX", "PEK"]),
    [3, 4, 5, 4, 3, 2, 1])

#       ATL DXB HND LAX
#     0  0   0   0   0
# ATL 0  0
# PEK 0
# LAX 0
# DXB 0
# HND 0
