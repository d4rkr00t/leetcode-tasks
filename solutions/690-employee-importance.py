# Employee Importance
# https://leetcode.com/problems/employee-importance/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def getImportance(employees: List, id: int) -> int:
    graph = {}

    for emp in employees:
        graph[emp.id] = emp

    def dfs(node):
        importance = graph[node].importance

        for sub in graph[node].subordinates:
            importance += dfs(sub)

        return importance

    return dfs(id)
