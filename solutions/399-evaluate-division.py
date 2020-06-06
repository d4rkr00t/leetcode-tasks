# Evaluate Division
# https://leetcode.com/problems/evaluate-division/
# medium
#
# Tags: Google, Amazon, Facebook
#
# Time:  O(Q * E+V)
# Space: O(E + V)
#
# Solution:
# BFS

def calcEquation(equations: [[str]], values: [float], queries: [[str]]) -> [float]:
    graph = {}

    for i in range(len(equations)):
        a,b = equations[i]
        v = values[i]

        graph[a] = graph[a] if a in graph else []
        graph[b] = graph[b] if b in graph else []

        graph[a].append((b, v))
        graph[a].append((a,1.0))
        graph[b].append((b, 1.0))
        graph[b].append((a, 1/v))

    def bfs(graph, start, target):
        if not start[0] in graph:
            return -1.0

        queue = [start]
        visited = set()

        while queue:
            cur = queue.pop(0)

            for con in graph[cur[0]]:
                if con[0] == target:
                    return con[1] * cur[1]
                elif con[0] not in visited:
                    queue.append((con[0], con[1] * cur[1]))
                    visited.add(con[0])

        return -1.0

    res = []
    for a,b in queries:
        res.append(bfs(graph, (a, 1.0), b))

    return res

#
# {
#   "a": [("a", 1), ("b", 2)],
#   "b": [("b", 1), ("a", 0.5), ("c", 3.0)],
#   "c": [("b", 0.33), ("c", 1)],
# }
#
#

print(calcEquation(
    equations = [ ["a", "b"], ["b", "c"] ],
    values = [2.0, 3.0],
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
), [6.0, 0.5, -1.0, 1.0, -1.0 ])
#   2    3
# a -> b -> c
#   <-   <-
#  0.5   0.33
