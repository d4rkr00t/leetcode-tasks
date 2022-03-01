# The Most Similar Path in a Graph
# https://leetcode.com/problems/the-most-similar-path-in-a-graph/
# hard
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def mostSimilar(n: int, roads: List[List[int]], names: List[str],
                targetPath: List[str]) -> List[int]:

    t = len(targetPath)
    dp = [[float("inf")] * n for _ in range(t)]
    graph = [[] for _ in range(n)]
    back = {}

    for fr, to in roads:
        graph[fr].append(to)
        graph[to].append(fr)

    for i in range(t):
        for j in range(n):
            cur = 0 if names[j] == targetPath[i] else 1

            if i == 0:
                dp[i][j] = cur
                continue

            prev = float("inf")
            for nei in graph[j]:
                if dp[i - 1][nei] < prev:
                    prev = dp[i - 1][nei]
                    back[i, j] = nei
                    dp[i][j] = cur + prev

    cur = 0
    for j in range(n):
        if dp[-1][j] < dp[-1][cur]:
            cur = j

    res = []
    for i in range(t - 1, -1, -1):
        res.append(cur)
        if i > 0:
            cur = back[i, cur]

    return res[::-1]


#         ATL PEK LAX DXB HND
#         0   1   2   3   4
# ATL 0   0   1   1   1   1
# DXB 1   2   2   1   0   2
# HND 2   1   1   3   3   2
# LAX 3   4   3   1   1   2

# print(
#     mostSimilar(n=5,
#                 roads=[[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
#                 names=["ATL", "PEK", "LAX", "DXB", "HND"],
#                 targetPath=["ATL", "DXB", "HND", "LAX"]), [0, 2, 4, 2])

print(
    mostSimilar(
        n=4,
        roads=[[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],
        names=["ATL", "PEK", "LAX", "DXB"],
        targetPath=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX"]),
    [0, 1, 0, 1, 0, 1, 0, 1])

# print(
#     mostSimilar(n=6,
#                 roads=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
#                 names=["ATL", "PEK", "LAX", "ATL", "DXB", "HND"],
#                 targetPath=["ATL", "DXB", "HND", "DXB", "ATL", "LAX", "PEK"]),
#     [3, 4, 5, 4, 3, 2, 1])
