# Reachable Nodes In Subdivided Graph
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
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
import heapq


def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
    graph = collections.defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = graph[v][u] = w

    pq = [(0, 0)]
    dist = {0: 0}
    used = {}
    ans = 0

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        # Each node is only visited once.  We've reached
        # a node in our original graph.
        ans += 1

        for nei, weight in graph[node].items():
            # M - d is how much further we can walk from this node;
            # weight is how many new nodes there are on this edge.
            # v is the maximum utilization of this edge.
            v = min(weight, maxMoves - d)
            used[node, nei] = v

            # d2 is the total distance to reach 'nei' (neighbor) node
            # in the original graph.
            d2 = d + weight + 1
            if d2 < dist.get(nei, maxMoves + 1):
                heapq.heappush(pq, (d2, nei))
                dist[nei] = d2

    # At the end, each edge (u, v, w) can be used with a maximum
    # of w new nodes: a max of used[u, v] nodes from one side,
    # and used[v, u] nodes from the other.
    for u, v, w in edges:
        ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

    return ans


print(
    reachableNodes(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], maxMoves=6, n=3),
    13)

print(
    reachableNodes(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]],
                   maxMoves=10,
                   n=4), 23)

# print(
#     reachableNodes(edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4],
#                           [3, 4, 5]],
#                    maxMoves=17,
#                    n=5), 1)

#          0
#      /4     \8
#    1    —6    2
#      \1
#        3
#
# hq = [(4,1,0),(8,2,0)]
# next = (4,1,0) | hq = [(8,2,0)] | ans = 0
# next = (?) | hq = [(5,3,4), (8,2,0), (10, 2, 4)] | ans = 0 + 5
# next = (5,3,4) | hq = [(8,2,0), (10, 2, 4)] | ans = 0 + 5
# next = (?) | hq = [(8,2,0), (10, 2, 4)] | ans = 0 + 5 + 2
# next = (8,2,0) | hq = [(10, 2, 4)] | ans = 0 + 5 + 2
# next = (?) | hq = [(10, 2, 4)] | ans = 0 + 5 + 2 + 9
# next = (10, 2, 4) | hq = [] | ans = 0 + 5 + 2 + 9 + 7
# ans = 23
