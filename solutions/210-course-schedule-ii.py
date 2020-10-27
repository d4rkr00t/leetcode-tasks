# Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# medium
#
# Tags: Amazon, Google, Microsoft, Facebook
#
# Time:  O(E+V)
# Space: O(E+V)
#
# Solution:
# Topological Sort

from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses
    ans = []
    cycle = False

    for d, c in prerequisites:
        graph[d].append(c)

    def dfs(node):
        nonlocal cycle
        visited[node] = 1

        for nei in graph[node]:
            if visited[nei] == 1:
                cycle = True
                return

            if visited[nei] == 0:
                dfs(nei)

        visited[node] = 2
        ans.append(node)

    for i in range(numCourses):
        if cycle:
            break

        if visited[i] == 0:
            dfs(i)

    ans

    return ans if not cycle else []


print(findOrder(2, [[1, 0]]), [0, 1])
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
      [0, 1, 2, 3], [0, 2, 1, 3])
