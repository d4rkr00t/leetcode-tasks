# Convert Binary Search Tree to Sorted Doubly Linked List
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# medium
#
# Tags: Facebook, Microsoft, Amazon
#
# Time:  O(n)
# Space: O(1) || O(h)
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
            return

        inorder(node.left)
        if not first:
            first = node
            last = node
        else:
            node.left = last
            last.right = node
            last = node

        inorder(node.right)

    inorder(root)

    first.left = last
    last.right = first

    return first


"""
–>        [4]
–>      2       [5]
–>  (1)    3

() – first
[] - last
{} – cur
"""
