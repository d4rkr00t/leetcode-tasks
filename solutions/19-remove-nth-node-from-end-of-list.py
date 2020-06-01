# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# medium
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    prev_idx = cur_idx = 0
    prev = cur = dummy = ListNode(0, head)

    while cur.next:
        cur_idx += 1
        cur = cur.next
        if cur_idx - prev_idx > n:
            prev_idx += 1
            prev = prev.next

    prev.next = prev.next.next

    return dummy.next

#                     |     |
# Given linked list: 1->2->3->4->5, and n = 2.

#                    |  |
# Given linked list: 1->2, and n = 2.
