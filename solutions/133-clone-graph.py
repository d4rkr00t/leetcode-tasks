# Clone Graph
# https://leetcode.com/problems/clone-graph/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(N+M)
# Space: O(N)
#
# Solution:
# DFS


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(self, node: Node) -> Node:
    table = {}

    def cloneNode(node):
        if node in table:
            return table[node]

        if not node:
            return None

        newNode = Node(node.val)
        table[node] = newNode

        for nei in node.neighbors:
            newNode.neighbors.append(cloneNode(nei))

        return newNode

    return cloneNode(node)
