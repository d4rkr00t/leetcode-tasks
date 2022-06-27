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
    tmpHead = ListNode(0, head)
    prev = tmpHead
    cur = tmpHead.next
    dist = 0
    while cur:
        if dist < n:
            cur = cur.next
            dist += 1
        else:
            prev = prev.next
            cur = cur.next

    if prev and prev.next:
        prev.next = prev.next.next

    return tmpHead.next
