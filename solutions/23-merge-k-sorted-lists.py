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
from Queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]) -> ListNode:
    if not lists:
        return None

    q = PriorityQueue()

    for l in lists:
        while l:
            q.put((l.val, l))
            l = l.next

    dummy = cur = ListNode()

    while not q.empty():
        (_, cur.next) = q.get()
        cur = cur.next

    return dummy.next
