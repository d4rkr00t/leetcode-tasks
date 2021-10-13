# Time Needed to Inform All Employees - LeetCode
# https://leetcode.com/problems/time-needed-to-inform-all-employees/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def numOfMinutes(n: int, headID: int, manager: List[int],
                 informTime: List[int]) -> int:

    queue = [headID]
    graph = [[] for _ in range(n)]
    informed = [0] * n
    ans = 0

    for i in range(n):
        mgr = manager[i]
        if mgr >= 0:
            graph[mgr].append(i)

    while queue:
        cur = queue.pop(-1)
        it = informTime[cur] + informed[cur]
        for nei in graph[cur]:
            informed[nei] = it
            ans = max(ans, it)
            queue.append(nei)

    return ans


print(numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]), 0)
print(
    numOfMinutes(n=6,
                 headID=2,
                 manager=[2, 2, -1, 2, 2, 2],
                 informTime=[0, 0, 1, 0, 0, 0]), 1)
print(
    numOfMinutes(n=7,
                 headID=6,
                 manager=[1, 2, 3, 4, 5, 6, -1],
                 informTime=[0, 6, 5, 4, 3, 2, 1]), 21)
print(
    numOfMinutes(n=15,
                 headID=0,
                 manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                 informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 3)
print(
    numOfMinutes(n=4,
                 headID=2,
                 manager=[3, 3, -1, 2],
                 informTime=[0, 0, 162, 914]), 1076)
