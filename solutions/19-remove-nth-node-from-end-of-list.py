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
    dist = 0
    dummy = ListNode(0, head)
    prev = cur = dummy

    while cur.next:
        cur = cur.next
        dist += 1

        if dist > n:
            dist -= 1
            prev = prev.next

    prev.next = prev.next.next

    return dummy.next
