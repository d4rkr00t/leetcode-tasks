# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# medium
#
# Tags: Amazon, Google, Facebook, Microsoft
#
# Time:  O(max(n, m))
# Space: TBD

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    cur = dummy
    carry = 0

    while l1 or l2:
        l1v = l1.val if l1 else 0
        l2v = l2.val if l2 else 0

        carry, sum = divmod(l1v + l2v + carry, 10)

        cur.next = ListNode(sum)
        cur = cur.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        cur.next = ListNode(carry)

    return dummy.next
