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


def accountsMerge(accounts: [[str]]) -> [[str]]:
    em_to_name = {}
    graph = {}

    for acc in accounts:
        name = acc.pop(0)
        for i in range(len(acc)):
            em_to_name[acc[i]] = name
            graph[acc[i]] = graph.get(acc[i], [])
            for j in range(i+1, len(acc)):
                graph[acc[j]] = graph.get(acc[j], [])
                graph[acc[i]].append(acc[j])
                graph[acc[j]].append(acc[i])

    def dfs(node, visited, ans):
        ans.append(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei, visited, ans)

    result = []
    visited = set()

    for k in graph.keys():
        if k not in visited:
            visited.add(k)
            ans = []
            dfs(k, visited, ans)
            result.append([em_to_name[ans[0]]] + sorted(ans))

    return result


print(accountsMerge(
    [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]),
    [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  [
        "John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
)
