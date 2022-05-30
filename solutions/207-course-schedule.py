# Course Schedule
# https://leetcode.com/problems/course-schedule/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses

    for f, t in prerequisites:
        graph[f].append(t)

    def dfs(node):
        if visited[node] == 1:
            return False

        visited[node] = 1

        for nei in graph[node]:
            if not dfs(nei):
                return False

        visited[node] = 2
        return True

    return dfs(0)


print(canFinish(numCourses=2, prerequisites=[[1, 0]]), True)
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]), False)
