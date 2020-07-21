# Evaluate Division
# https://leetcode.com/problems/evaluate-division/
# medium
#
# Tags: Google, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def calcEquation(equations: [[str]], values: [float], queries: [[str]]) -> [float]:
    graph = {}

    # Build grapg
    for eqn, w in zip(equations, values):
        x, y = eqn
        graph[x] = graph.get(x, [])
        graph[y] = graph.get(y, [])

        graph[x].append((y, w))
        graph[y].append((x, 1/w))

    # BFS
    def bfs(s, t):
        visited = set([s])
        queue = [(s, 1)]

        while queue:
            c, w = queue.pop(0)

            if c not in graph:
                continue

            for n, w2 in graph[c]:
                if n == t:
                    return w*w2

                if n not in visited:
                    visited.add(n)
                    queue.append((n, w*w2))

        return -1.0

    ans = []
    for s, t in queries:
        ans.append(bfs(s, t))

    return ans


print(calcEquation(
    equations=[["a", "b"], ["b", "c"]],
    values=[2.0, 3.0],
    queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
), [6.0, 0.5, -1.0, 1.0, -1.0])
