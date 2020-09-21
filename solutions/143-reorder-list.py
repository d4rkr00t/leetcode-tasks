# Reorder List
# https://leetcode.com/problems/reorder-list/
# medium
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    def find_mid(head):
        s, f = head

        while f and f.next:
            s = s.next
            f = f.next.next

        return s

    def reverse_list(node):
        prev = None
        cur = node
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    mid = find_mid(head)
    reversed_tail = reverse_list(mid.next)

    while reversed_tail:
        next = head.next
        head.next = reversed_tail

        reversed_tail = next
        head = head.next

#           |
# 1 -> 7 -> 2 -> 3 -> 4
# 6 -> 5
