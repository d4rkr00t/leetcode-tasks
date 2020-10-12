# Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# easy
#
# Tags: Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    pa = headA
    pb = headB

    while pa != pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA

    return pa
