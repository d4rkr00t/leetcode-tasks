# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# medium
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dist = 0
    l = 1
    prev = cur = head

    while cur.next:
        dist += 1
        l += 1
        cur = cur.next
        if dist > n:
            prev = prev.next
            dist -= 1

    if n == l:
        return head.next

    if prev.next:
        prev.next = prev.next.next

    return head
