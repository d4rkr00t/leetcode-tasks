# Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# medium
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def findOrder(numCourses: int, prerequisites: [[int]]) -> [int]:
    graph = [[] for _ in range(numCourses)]

    for c, d in prerequisites:
        graph[c].append(d)

    order = []
    visited = [0] * numCourses
    cycle = False

    def dfs(start):
        nonlocal visited, order, cycle
        if cycle:
            return

        visited[start] = 1

        for dep in graph[start]:
            if visited[dep] == 1:
                cycle = True
                return False

            if visited[dep] == 0:
                dfs(dep)

        visited[start] = 2
        order.append(start)

    for i in range(numCourses):
        if visited[i] == 0:
            dfs(i)

    return order if not cycle else []


print(findOrder(2, [[1, 0]]), [0, 1])
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
      [0, 1, 2, 3], [0, 2, 1, 3])
