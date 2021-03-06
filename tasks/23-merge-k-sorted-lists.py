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
    if not lists:
        return []

    hq = []
    for l in lists:
        while l:
            heapq.heappush((l.val, l))
            l = l.next

    head = cur = heapq.heappop(hq)

    while hq:
        tmp = heapq.heappop(hq)
        cur.next = tmp
        tmp.next = None
        cur = cur.next

    return head
