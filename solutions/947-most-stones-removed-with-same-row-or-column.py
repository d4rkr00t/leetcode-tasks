# Most Stones Removed with Same Row or Column
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# medium
#
# Tags: Google
#
# Time:  O(n log n)
# Space: O(n)
#
# Solution:
# Union Find

def removeStones(stones: [[int]]) -> int:
    graph = {}

    for f,t in stones:
        t = t + 10000
        if not f in graph: graph[f] = (f, 0)
        if not t in graph: graph[t] = (t, 0)

        tgt = graph[t][0]
        while tgt != graph[tgt][0]:
            tgt = graph[tgt][0]

        src = graph[f][0]
        while src != graph[src][0]:
            src = graph[src][0]

        if tgt == src:
            graph[tgt] = (tgt, graph[tgt][1] + 1)
        else:
            graph[src] = (src, graph[src][1] + graph[tgt][1] + 1)
            graph[tgt] = (src, 0)


    ans = 0
    for k,v in graph.values():
        ans += max(v - 1, 0)

    return ans



print(removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]), 5)
print(removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]), 3)
print(removeStones([[0,0]]), 0)

#   0, 2, 2
#   1, 0, 0
#
# [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 0,0 -> 0,1 -> 1,0 -> 1,2 -> 2,1 -> 2,2
# [[0,0],[0,2],[1,1],[2,0],[2,2]]
# 0 1 0
# 4 1 0
#
#
# 0,0 -> 0,2 -> 2,0 -> 2,2
# 1,1
