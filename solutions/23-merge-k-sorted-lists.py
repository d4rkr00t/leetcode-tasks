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
    hq = []

    for i, l in enumerate(lists):
        if l:
            heapq.heappush(hq, (l.val, i))

    head = ListNode()
    cur = head

    while hq:
        _, idx = heapq.heappop(hq)
        tmp = lists[idx]
        cur.next = tmp
        cur = cur.next

        if tmp.next:
            lists[idx] = tmp.next
            heapq.heappush(hq, (tmp.next.val, idx))

    return head.next
