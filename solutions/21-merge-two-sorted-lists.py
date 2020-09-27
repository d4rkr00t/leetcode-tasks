# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# easy
#
# Tags: Amazon, Microsoft, Google
#
# Time:  O(n) – where n – is a length of a longest list
# Space: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = cur = ListNode(0)

    while l1 or l2:
        l1v = l1.val if l1 else float("inf")
        l2v = l2.val if l2 else float("inf")

        if l1v < l2v:
            cur.next = ListNode(l1v)
            l1 = l1.next
        else:
            cur.next = ListNode(l2v)
            l2 = l2.next

        cur = cur.next

    return head.next
