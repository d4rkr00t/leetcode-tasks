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

from collections import defaultdict
from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    emailToEmail = defaultdict(set)
    emailToName = {}
    visited = set()

    def dfs(key, res=set()):
        res.add(key)
        visited.add(key)

        if key not in emailToEmail:
            return res

        for nei in emailToEmail[key]:
            if nei in visited: continue
            dfs(nei, res)

        return res

    for accData in accounts:
        name = accData.pop(0)
        for e1 in accData:
            if not e1 in emailToEmail:
                emailToEmail[e1] = set()

            for e2 in accData:
                if e1 != e2:
                    emailToEmail[e1].add(e2)
                    emailToEmail[e2].add(e1)
            emailToName[e1] = name

    res = []
    for key in emailToEmail.keys():
        if key in visited: continue

        temp = set()
        dfs(key, temp)
        temp = list(temp)
        temp.sort()
        res.append([emailToName[key]] + temp)

    return res


print(
    accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"],
                   ["John", "johnnybravo@mail.com"],
                   ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                   ["Mary", "mary@mail.com"]]),
    [[
        "John", 'john00@mail.com', 'john_newyork@mail.com',
        'johnsmith@mail.com'
    ], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]])

# print(
#     accountsMerge([["David", "David0@m.co", "David1@m.co"],
#                    ["David", "David3@m.co", "David4@m.co"],
#                    ["David", "David4@m.co", "David5@m.co"],
#                    ["David", "David2@m.co", "David3@m.co"],
#                    ["David", "David1@m.co", "David2@m.co"]]))
