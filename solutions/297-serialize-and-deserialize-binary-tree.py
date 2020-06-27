# Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# hard
#
# Tags: Facebook, Microsoft, Amazon, Google
#
# Time:  O(n)
# Space: O(h)
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

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root: return "X"

        res = str(root.val)
        res += "," + self.serialize(root.left)
        res += "," + self.serialize(root.right)

        return res

    def __deserialize_preorder__(self, data, pos):
        if pos >= len(data) or data[pos] == "X":
            return (None, pos+1)

        node = TreeNode(int(data[pos]))
        node.left, pos = self.__deserialize_preorder__(data, pos + 1)
        node.right, pos = self.__deserialize_preorder__(data, pos)

        return (node, pos)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data: return None

        return self.__deserialize_preorder__(data.split(","), 0)[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
