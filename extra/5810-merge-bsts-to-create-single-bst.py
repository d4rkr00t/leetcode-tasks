# Merge BSTs to Create Single BST
# https://leetcode.com/problems/merge-bsts-to-create-single-bst/
# hard
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# HashTable, Binary Search

from typing import List
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def canMerge(trees: List[TreeNode]) -> TreeNode:
    m = {}
    cnt = Counter()
    minv = float("-inf")
    maxv = float("inf")

    def traverse(r, m, min_left, max_right):
        if not r:
            return True

        if r.val <= min_left or r.val >= max_right:
            return False

        if r.left == r.right:
            it = m.get(r.val, None)
            if it and r != it:
                r.left = it.left
                r.right = it.right
                del m[r.val]

        return traverse(r.left, m, min_left, r.val) and traverse(
            r.right, m, r.val, max_right)

    for t in trees:
        m[t.val] = t
        cnt[t.val] += 1

        if t.left:
            cnt[t.left.val] += 1

        if t.right:
            cnt[t.right.val] += 1

    for t in trees:
        if cnt[t.val] == 1:
            if traverse(t, m, minv, maxv) and len(m.keys()) == 1:
                return t

    return None
