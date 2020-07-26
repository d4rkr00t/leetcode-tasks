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

def canFinish(numCourses: int, prerequisites: [[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses
    cycle = False

    for c, d in prerequisites:
        graph[c].append(d)

    def dfs(c):
        nonlocal visited, cycle
        if cycle:
            return

        visited[c] = 1

        for dep in graph[c]:
            if visited[dep] == 1:
                cycle = True
                return

            if visited[dep] == 0:
                dfs(dep)

        visited[c] = 2

    for i in range(numCourses):
        if cycle:
            break

        if visited[i] == 0:
            dfs(i)

    return not cycle


print(canFinish(numCourses=2, prerequisites=[[1, 0]]), True)
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]), False)
