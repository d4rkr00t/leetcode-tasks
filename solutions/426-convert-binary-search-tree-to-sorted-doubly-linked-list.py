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
    first = None
    last = None

    def inorder(node):
        nonlocal first, last

        if not node:
            return None

        inorder(node.left)

        if last:
            last.right = node
            node.left = last
        else:
            first = node

        last = node

        inorder(node.right)

    inorder(root)

    if first:
        last.right = first
        first.left = last

    return first
