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
    links = {[node.val]: Node(node.val)}
    queue = [node]

    while queue:
        node = queue.pop(0)
        new_node = links[node.val]

        for n in node.neighbors:
            if n.val in links:
                new_node.neighbors.append(links[n.val])
                continue

            nn = Node(n.val)
            links[n.val] = nn
            new_node.neighbors.append(nn)
            queue.append(n)

    return links[node.val]
