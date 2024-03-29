# Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# medium
#
# Tags: Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    return root1.val == root2.val and (
        (flipEquiv(root1.left, root2.left)
         and flipEquiv(root1.right, root2.right)) or
        (flipEquiv(root1.left, root2.right)
         and flipEquiv(root1.right, root2.left)))
