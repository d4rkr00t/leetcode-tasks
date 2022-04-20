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

from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses
    ans = []

    for t, f in prerequisites:
        graph[t].append(f)

    def dfs(node):
        if visited[node] == 1:
            return False

        if visited[node] == 2:
            return True

        visited[node] = 1

        for nei in graph[node]:
            if not dfs(nei):
                return False

        ans.append(node)
        visited[node] = 2
        return True

    for node in range(numCourses):
        if not dfs(node):
            return []

    return ans


print(findOrder(2, [[1, 0]]), [0, 1])
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3],
      [0, 2, 1, 3])
