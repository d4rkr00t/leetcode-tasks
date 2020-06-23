# Course Schedule
# https://leetcode.com/problems/course-schedule/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(E+V)
# Space: O(E+V)

def canFinish(numCourses: int, prerequisites: [[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]

    for f,t in prerequisites:
        graph[f].append(t)

    visited = [0] * numCourses
    is_possible = True

    def dfs(node):
        nonlocal visited, is_possible
        visited[node] = 1

        for c in graph[node]:
            if visited[c] == 1:
                is_possible = False
                return

            if visited[c] == 0:
                dfs(c)

        visited[node] = 2

    for i in range(numCourses):
        if visited[i] == 0 and is_possible:
            dfs(i)

    return is_possible

print(canFinish(numCourses = 2, prerequisites = [[1,0]]), True)
print(canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]), False)
