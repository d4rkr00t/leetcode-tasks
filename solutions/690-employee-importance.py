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

    def dfs(id):
        emp = graph[id]
        res = emp.importance

        for sub in emp.subordinates:
            res += dfs(sub)

        return res

    return dfs(id)
