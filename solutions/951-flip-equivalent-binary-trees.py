# Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# medium
#
# Tags: Google
#
# Time:  O(n)
# Space: O(n)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
    if root1.val != root2.val:
        return False

    return (self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)) or (
                self.flipEquiv(root1.left, root2.left)
                and self.flipEquiv(root1.right, root2.right))
