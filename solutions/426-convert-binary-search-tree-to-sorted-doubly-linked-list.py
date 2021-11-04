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


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeToDoublyList(self, root: Node) -> Node:
    first = last = None

    def inorder(node):
        nonlocal first, last

        if not node:
            return

        inorder(node.left)

        if last:
            last.right = node
            node.left = last
        else:
            first = node

        last = node
        inorder(node.right)

    if not root:
        return None

    inorder(root)

    first.left = last
    last.right = first

    return first


#        4      |
#    2       5  | cur
# 1    3        | first prev
#
# None <– 1 -> 2 <-> 4 -> None
