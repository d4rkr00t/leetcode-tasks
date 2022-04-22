# Time Needed to Inform All Employees
# https://leetcode.com/problems/time-needed-to-inform-all-employees/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from collections import defaultdict
from typing import List


# S: O(n)
# T: O(n)
def numOfMinutes(n: int, headID: int, manager: List[int],
                 informTime: List[int]) -> int:
    # S: O(n)
    graph = defaultdict(list)

    # T: O(n)
    for i, m in enumerate(manager):
        if m == -1:
            continue

        graph[m].append(i)

    # S: O(n)
    # T: O(n)
    def dfs(node, elapsed):
        time = res = elapsed + informTime[node]

        for child in graph[node]:
            res = max(res, dfs(child, time))

        return res

    return dfs(headID, 0)


# print(numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]), 0)
# print(
#     numOfMinutes(n=6,
#                  headID=2,
#                  manager=[2, 2, -1, 2, 2, 2],
#                  informTime=[0, 0, 1, 0, 0, 0]), 1)

print(
    numOfMinutes(n=15,
                 headID=0,
                 manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                 informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 3)
