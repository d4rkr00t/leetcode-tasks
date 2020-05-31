# Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# medium
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  O(E+V)
# Space: O(N) where N is numCourses
#
# Solution:
# DFS

def findOrder(numCourses: int, prerequisites: [[int]]) -> [int]:
    graph = [[] for _ in range(numCourses)]

    for t,f in prerequisites:
        graph[t].append(f)

    order = []
    processed = [0] * numCourses
    is_possible = True

    def dfs(node):
        nonlocal graph, order, processed, is_possible

        if not is_possible:
            return False

        processed[node] = 1

        for edge in graph[node]:
            if processed[edge] == 1: # cycle
                is_possible = False
                return False
            elif processed[edge] == 0:
                dfs(edge)

        processed[node] = 2
        order.append(node)

    for i in range(numCourses):
        if processed[i] == 0:
            dfs(i)

    return order if is_possible else []


print(findOrder(2, [[1,0]]), [0,1])
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3], [0,2,1,3])

#
# 0 -> 1,2
# 1 -> 3
#
