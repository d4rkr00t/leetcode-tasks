# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# hard
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]) -> ListNode:
    head = next = ListNode()
    pq = []

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(pq, (l.val, i, l))

    i = len(lists)
    while pq:
        val, idx, node = heapq.heappop(pq)

        next.next = ListNode(val)
        next = next.next

        if node.next:
            heapq.heappush(pq, (node.next.val, i+1, node.next))
            i += 1

    return head.next
