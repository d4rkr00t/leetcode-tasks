# Reorder List
# https://leetcode.com/problems/reorder-list/
# medium
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  O(n)
# Space: O(1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    def reverse(node):
        prev = None
        cur = node
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first, second = head, reverse(slow)
    while second.next:
        tmp = first.next
        first.next = second
        first = tmp

        tmp = second.next
        second.next = first
        second = tmp

    return head


# 1 -> 2 -> 3
# H
#
# 5 -> 4 -> 3
# S
#
#
