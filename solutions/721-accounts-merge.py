# Accounts Merge
# https://leetcode.com/problems/accounts-merge/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    email_to_name = {}
    graph = {}
    for acc in accounts:
        name = acc.pop(0)
        for i, email in enumerate(acc):
            email_to_name[email] = name
            graph[email] = graph.get(email, [])
            graph[email].extend(acc[:i] + acc[i+1:])

    def dfs(node, group, visited):
        visited.add(node)
        group.append(node)

        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, group, visited)

        return group

    res = []
    visited = set()

    for email in email_to_name.keys():
        if email not in visited:
            group = dfs(email, [], visited)
            if group:
                res.append([email_to_name[group[0]]] + sorted(group))

    return res


print(accountsMerge(
    [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]),
    [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
        ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
)
