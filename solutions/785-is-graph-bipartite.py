# Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/
# medium
#
# Tags: Facebook, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isBipartite(graph: [[int]]) -> bool:
    visited = [0] * len(graph)

    for i in range(len(graph)):
        if visited[i] == 0:
            queue = [i]
            visited[i] = 1

            while queue:
                cur = queue.pop(0)
                next_color = 2 if visited[cur] == 1 else 1

                for nei in graph[cur]:
                    if visited[nei] == 0:
                        queue.append(nei)
                        visited[nei] = next_color
                    elif visited[nei] == visited[cur]:
                        return False

    return True

print(isBipartite([[1,3], [0,2], [1,3], [0,2]]), True)
print(isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]), False)


