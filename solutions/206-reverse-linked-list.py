# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# easy
#
# Tags: Amazon, Microsoft, Google, Facebook
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Pointers magic


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    cur = head
    prev = None

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev
