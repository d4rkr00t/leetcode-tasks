# Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# medium
#
# Tags: Facebook, Amazon, Google, Microsoft
#
# Time:  O(N * log(N))
# Space: O(N)
#
# Solution:
# TBD

def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    table = {}

    def dfs(node, level):
        nonlocal table

        if not node: return

        table[level] = table.get(level, [])

        table[level].append(node.val)

        dfs(node.left, level - 1)
        dfs(node.right, level + 1)

    dfs(root, 0)

    ans = []

    for k in sorted(table.keys()):
        ans.append(table[k])

    return ans
