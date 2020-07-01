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
# TBD

def alienOrder(words: [str]) -> str:
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

        if i == len(w2) and len(w1) > len(w2):
            return ""

        if i < len(w1) and i < len(w2):
            graph[w1[i]] = graph.get(w1[i], set())
            graph[w1[i]].add(w2[i])
        w1 = w2

    ans = ""
    seen = {}
    is_cycle = False

    def dfs(node):
        nonlocal seen, is_cycle, ans

        if is_cycle: return

        seen[node] = 1

        for nei in graph[node]:
            if nei not in seen:
                dfs(nei)
            elif seen[nei] == 1:
                is_cycle = True
                return

        seen[node] = 2
        ans = node + ans


    for c in graph.keys():
        if c not in seen:
            dfs(c)

    return "" if is_cycle else ans


print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")
print(alienOrder(["z", "x"]), "zx")
print(alienOrder(["z", "x", "z"]), "")
