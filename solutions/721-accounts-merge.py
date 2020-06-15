# Accounts Merge
# https://leetcode.com/problems/accounts-merge/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(V+E)
# Space: O(V+E)
#
# Solution:
# DFS

import collections

def accountsMerge(accounts: [[str]]) -> [[str]]:
    em_to_name = {}
    graph = collections.defaultdict(set)

    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            em_to_name[email] = name

    seen = set()
    ans = []

    for email in graph:
        if email not in seen:
            seen.add(email)

            stack = [email]
            component = []

            while stack:
                cur = stack.pop()
                component.append(cur)

                for nei in graph[cur]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)

            ans.append([em_to_name[email]] + sorted(component))

    return ans


print(accountsMerge(
    [
        ["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]),
    [
        ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
        ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
)
