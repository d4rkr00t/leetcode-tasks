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

def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    first = head
    second = prev

    while second.next:
        tmp = first.next
        first.next = second
        first = tmp

        tmp = second.next
        second.next = first
        second = tmp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


1 -> 2 -> 3

prev = None
cur = 1
tmp = 2
