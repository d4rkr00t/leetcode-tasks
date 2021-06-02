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
# Top Sort

from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]

    for to, fr in prerequisites:
        graph[to].append(fr)

    visited = [0] * numCourses

    def dfs(cur):
        if visited[cur] == 1:
            # Cycle
            return True

        visited[cur] = 1
        for nei in graph[cur]:
            if visited[nei] != 2:
                cycle = dfs(nei)
                if cycle:
                    return cycle

        visited[cur] = 2

        return False

    for i in range(numCourses):
        if visited[i] == 0:
            cycle = dfs(i)
            if cycle:
                return False

    return True


print(canFinish(numCourses=2, prerequisites=[[1, 0]]), True)
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]), False)
