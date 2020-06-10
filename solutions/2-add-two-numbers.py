# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# medium
#
# Tags: Amazon, Google, Facebook, Microsoft
#
# Time:  O(n+m)
# Space: O(n)
#
# Solution:
# TBD

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = pointer = ListNode()
    carry = 0

    while l1 or l2 or carry:
        l1v = l1.val if l1 else 0
        l2v = l2.val if l2 else 0

        val = l1v+l2v+carry
        carry = val // 10

        if l1: l1 = l1.next
        if l2: l2 = l2.next

        pointer.next = ListNode(val % 10)
        pointer = pointer.next

    return head.next

