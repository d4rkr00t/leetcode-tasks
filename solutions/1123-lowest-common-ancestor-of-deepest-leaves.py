# Lowest Common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# medium
#
# Tags: Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(root):
        if not root: return 0, None
        h1, lca1 = helper(root.left)
        h2, lca2 = helper(root.right)
        if h1 > h2: return h1 + 1, lca1
        if h1 < h2: return h2 + 1, lca2
        return h1 + 1, root

    return helper(root)[1]
