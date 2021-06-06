# Accounts Merge
# https://leetcode.com/problems/accounts-merge/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(n + E+V)
# Space: O(n + E+V)
#
# Solution:
# TBD

from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    graph = {}
    email_to_name = {}
    visited = set()

    for acc in accounts:
        name = acc.pop(0)
        prev = None

        for email in acc:
            email_to_name[email] = name
            graph[email] = graph.get(email, [])
            if prev:
                graph[prev].append(email)
                graph[email].append(prev)

            prev = email

    def bfs(node):
        group = set()
        queue = [node]

        while queue:
            cur = queue.pop(0)
            visited.add(cur)
            group.add(cur)
            for nei in graph.get(cur, []):
                if nei not in visited:
                    queue.append(nei)

        return list(group)

    res = []
    for key in graph.keys():
        if key not in visited:
            res.append(bfs(key))

    return [[email_to_name[item[0]]] + item for item in res]


print(
    accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"],
                   ["John", "johnnybravo@mail.com"],
                   ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                   ["Mary", "mary@mail.com"]]),
    [[
        "John", 'john00@mail.com', 'john_newyork@mail.com',
        'johnsmith@mail.com'
    ], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]])
