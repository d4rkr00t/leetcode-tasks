# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# hard
#
# Tags: Microsoft, Amazon, Facebook
#
# Time:  O(n)
# Space: O(n/k) recursive call stack
#
# Solution:
# Recursion

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, tail):
    prev = None
    cur = head

    while cur != tail:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    cur = head
    count = k
    while count and cur:
        cur = cur.next
        count -= 1

    if count > 0:
        return head

    revHead = reverseBetween(head, cur)
    head.next = reverseKGroup(cur, k)

    return revHead
