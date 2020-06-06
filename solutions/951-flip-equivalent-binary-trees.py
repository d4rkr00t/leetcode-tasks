# Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# medium
#
# Tags: Google
#
# Time:  O(min(N1, N2))
# Space: O(min(h1, h2))
#
# Solution:
# TBD

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 == None and root2 == None: return True
    if root1 == None or root2 == None: return False
    return root1.val == root2.val and
        ((self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)) or
            (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)))
