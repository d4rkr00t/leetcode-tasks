# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# medium
#
# Tags: Amazon, Google, Facebook, Microsoft
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


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = cur = ListNode()
    carry = 0
    while l1 or l2:
        l1n = 0 if not l1 else l1.val
        l2n = 0 if not l2 else l2.val

        carry, val = divmod(l1n + l2n + carry, 10)
        cur.next = ListNode(val)
        cur = cur.next

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

    if carry:
        cur.next = ListNode(carry)

    return head.next
