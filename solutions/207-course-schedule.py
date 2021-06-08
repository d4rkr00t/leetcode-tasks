# Course Schedule
# https://leetcode.com/problems/course-schedule/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(E+V)
# Space: O(E+V)
#
# Solution:
# Cycles

from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    visited = [0] * numCourses
    graph = [[] for _ in range(numCourses)]
    for t, f in prerequisites:
        graph[t].append(f)

    def dfs(node):
        visited[node] = 1

        for nei in graph[node]:
            if visited[nei] == 1:
                return False
            elif visited[nei] == 2:
                continue

            if not dfs(nei):
                return False

        visited[node] = 2
        return True

    for i in range(numCourses):
        if visited[i] == 0:
            if not dfs(i):
                return False

    return True


print(canFinish(numCourses=2, prerequisites=[[1, 0]]), True)
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]), False)
