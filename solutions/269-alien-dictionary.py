# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
# hard
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Topological Sort

def alienOrder(words: [str]) -> str:
    cycle = False
    order = ""
    visited = {}
    graph = {}

    w1 = words[0]
    for c in w1:
        graph[c] = set()

    for j in range(1, len(words)):
        w2 = words[j]
        i = 0

        for c in w2:
            graph[c] = graph.get(c, set())

        while i < len(w1) and i < len(w2) and w1[i] == w2[i]:
            i += 1

        if i < len(w1) and i < len(w2) and i == len(w2) and len(w1) > len(w2):
            return ""

        if i < len(w1) and i < len(w2):
            graph[w1[i]] = graph.get(w1[i], set())
            graph[w1[i]].add(w2[i])
        w1 = w2

    def dfs(node):
        nonlocal order, visited, cycle
        visited[node] = 1

        if cycle:
            return

        if node in graph:
            for c in graph[node]:
                if c in visited and visited[c] == 1 and c != node:
                    cycle = True
                    return

                if c not in visited:
                    dfs(c)

        visited[node] = 2
        order = node + order

    for node in graph.keys():
        if node not in visited:
            dfs(node)

    return order if not cycle else ""


print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")
print(alienOrder(["z", "x"]), "zx")
print(alienOrder(["z", "x", "z"]), "")
print(alienOrder(["z", "z"]), "z")
