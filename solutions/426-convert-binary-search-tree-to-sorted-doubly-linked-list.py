# Convert Binary Search Tree to Sorted Doubly Linked List
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# medium
#
# Tags: Facebook, Microsoft, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def treeToDoublyList(self, root: 'Node') -> 'Node':
    first = last = None

    def dfs(node):
        nonlocal first, last
        if not node: return

        dfs(node.left)

        if last:
            last.right = node
            node.left = last
        else:
            first = node

        last = node

        dfs(node.right)

    dfs(root)

    if first:
        first.left = last
        last.right = first

    return first

#     5
#   2   6
#  1 3
# 0   4

