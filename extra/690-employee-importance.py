# Employee Importance
# https://leetcode.com/problems/employee-importance/
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
import collections


def getImportance(employees: List, id: int) -> int:
    table = {}

    for e in employees:
        table[e.id] = (e.importance, e.subordinates)

    def dfs(id):
        if id not in table:
            return 0

        (importance, subordinates) = table[id]

        return importance + sum([dfs(subid) for subid in subordinates])

    return dfs(id)
