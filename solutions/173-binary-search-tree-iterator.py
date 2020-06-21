# Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
# medium
#
# Tags: Facebook, Amazon, Microsoft, Google
#
# Time:  O(N)
# Space: O(h)
#
# Solution:
# TBD

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [root]


    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.hasNext():
            return None

        node = self.stack[-1]

        while node and node.left:
            self.stack.append(node.left)
            node = node.left

        node = self.stack.pop()

        if node.right:
            self.stack.append(node.right)

        return node.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.stack else False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
