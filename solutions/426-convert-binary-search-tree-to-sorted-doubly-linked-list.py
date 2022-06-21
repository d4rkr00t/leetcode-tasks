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
    first = cur = None

    def inorder(node):
        nonlocal first, cur
        if not node:
            return

        if not node.left and not node.right:
            first = node
            cur = node
            return

        inorder(node.left)

        cur.right = node
        node.left = cur
        cur = node

        inorder(node.right)

    inorder(root)

    cur.right = first
    first.left = cur

    return first
