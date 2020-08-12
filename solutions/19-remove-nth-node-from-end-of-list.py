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
    cur = prev = next = head
    dist = 0

    while next:
        next = next.next
        dist += 1

        if dist > n:
            prev = cur
            cur = cur.next
            dist -= 1

    if cur == head:
        return head.next

    prev.next = cur.next
    return head
