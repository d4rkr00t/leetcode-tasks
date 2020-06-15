# Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  O(V+E)
# Space: O(E)
#
# Solution:
# DFS

def isBipartite(graph: [[int]]) -> bool:
    colors = [0] * len(graph)

    def dfs(node, color):
        nonlocal colors, graph

        colors[node] = color
        next_color = 1 if color == 2 else 2

        for n in graph[node]:
            if colors[n] == color:
                return False

            if colors[n] != next_color:
                if not dfs(n, next_color):
                    return False

        return True

    for i in range(len(graph)):
        if colors[i] == 0:
            if not dfs(i, 1):
                return False

    return True

print(isBipartite([[1,3], [0,2], [1,3], [0,2]]), True)
print(isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]), False)


