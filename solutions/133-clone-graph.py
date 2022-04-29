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
    clones = {}

    def dfs(node):
        if node in clones:
            return clones[node]

        newnode = Node(node.val)
        clones[node] = newnode
        neighbours = []

        for nei in node.neighbors:
            neighbours.append(dfs(nei))

        newnode.neighbors = neighbours

        return newnode

    return dfs(node)
