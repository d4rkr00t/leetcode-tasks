# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# easy
#
# Tags: Amazon, Microsoft, Google, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head: ListNode) -> ListNode:
    if not head: return

    prev = None
    cur = head

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev

# 1 2 3 4 5
# 0 -> 2 -> 1
