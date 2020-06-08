# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# hard
#
# Tags: Amazon, Facebook, Microsoft, Google
#
# Time:  O(n * log(k))
# Space: O(k)
#
# Solution:
# TBD

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

def mergeKLists(self, lists: [ListNode]) -> ListNode:
    head = next = ListNode()
    pq = [(l.val, l) for l in lists if l]

    while pq:
        val, node = heapq.heappop(pq)

        next.next = ListNode(val)
        next = next.next

        if node:
            heapq.heappush(pq, (node.val, node))

    return head.next

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
