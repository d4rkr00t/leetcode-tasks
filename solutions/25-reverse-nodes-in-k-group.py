# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# hard
#
# Tags: Microsoft, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for singly-linked list.
from re import L


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    newHead = ListNode(0, head)
    tmpHead = newHead

    def reverse(fr, to):
        pass

    while True:
        steps = k
        node = tmpHead
        while steps and node.next:
            steps -= 1
            node = node.next

        print(tmpHead, node)

        break

    return newHead.next


# k = 3
#        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
# nh  ->
# cur -> 1 -> 2 -> 3
#        3 -> 2 -> 1 -> 4
