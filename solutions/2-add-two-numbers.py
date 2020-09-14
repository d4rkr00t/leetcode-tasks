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
    carry = 0
    head = cur = ListNode()

    while l1 or l2:
        l1v = l1.val if l1 else 0
        l2v = l2.val if l2 else 0
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        carry, val = divmod(l1v + l2v + carry, 10)
        cur.next = ListNode(val)
        cur = cur.next

    if carry:
        cur.next = ListNode(carry)

    return head.next
