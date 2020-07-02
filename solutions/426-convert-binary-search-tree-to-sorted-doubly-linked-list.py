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
    if not root:
        return None

    def inorder(node):
        nonlocal first, last

        if not node: return

        inorder(node.left)

        if last:
            last.right = node
            node.left = last
        else:
            first = node

        last = node

        inorder(node.right)

    first = None
    last = None
    inorder(root)
    last.right = first
    first.left = last

    return first

