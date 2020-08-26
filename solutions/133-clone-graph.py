# Clone Graph
# https://leetcode.com/problems/clone-graph/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(self, node: Node) -> Node:
    if not node:
        return None

    ht = {}
    root = Node(node.val)
    ht[node] = root
    queue = [node]

    while queue:
        cur = queue.pop(0)
        cloned = ht.get(cur)

        for nei in cur.neighbors:
            nei_cl = ht.get(nei, Node(nei.val))
            cloned.neighbors.append(nei_cl)

            if nei not in ht:
                queue.append(nei)

            ht[nei] = nei_cl

    return root
