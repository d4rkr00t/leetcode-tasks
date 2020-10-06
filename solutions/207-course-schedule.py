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
import collections


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)

    for c, d in prerequisites:
        graph[c].append(d)

    visited = [0] * numCourses
    cycle = False

    def dfs(c):
        nonlocal cycle

        if cycle:
            return False

        visited[c] = 1

        for nei in graph[c]:
            if visited[nei] == 1:
                cycle = True
                return False

            if visited[nei] == 0:
                dfs(nei)

        visited[c] = 2

    for i in range(numCourses):
        if visited[i] == 0:
            dfs(i)

    if cycle:
        return False

    return True


print(canFinish(numCourses=2, prerequisites=[[1, 0]]), True)
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]), False)
