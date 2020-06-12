# Clone Graph
# https://leetcode.com/problems/clone-graph/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(V+E)
# Space: O(V)
#
# Solution:
# BFS + HashTable

def cloneGraph(self, node: 'Node') -> 'Node':
    hm = {}
    queue = [node]

    while queue:
        cur = queue.pop(0)
        if cur.val not in hm:
            hm[cur.val] = Node(cur.val)

        for n in cur.neighbors:
            if n.val not in hm:
                hm[n.val] = Node(n.val)
                queue.append(n)

            hm[cur.val].neighbors.append(hm[n.val])

    return hm[1] if 1 in hm else None


# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

