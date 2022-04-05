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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    cur = head

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev


#   1 -> 2 -> 3
#       |     T
#       P
#   2 -> 1 -> None
