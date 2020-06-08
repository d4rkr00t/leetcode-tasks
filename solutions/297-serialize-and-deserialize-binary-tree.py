lear# Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  O(N)
# Space: O(N)
#
# Solution:
# Preorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize_preorder(self, node):
        if not node:
            return "X"

        return str(node.val) + "," + \
            self.serialize_preorder(node.left) + "," + \
                self.serialize_preorder(node.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.serialize_preorder(root)

    def deserialize_preorder(self, pos, nodes):
        if pos >= len(nodes):
            return (None, pos)

        raw_val = nodes[pos]
        pos += 1

        if raw_val == "X":
            return (None, pos)

        node = TreeNode(int(raw_val))

        node.left, pos = self.deserialize_preorder(pos, nodes)
        node.right, pos = self.deserialize_preorder(pos, nodes)

        return (node, pos)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.deserialize_preorder(0, data.split(","))[0]

#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 1,2,X,X,3,4,X,X,5,X,X
#         ^
