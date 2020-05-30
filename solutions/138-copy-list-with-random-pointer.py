# Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    dummy = Node()

    cur = head

    while cur:
        next = cur.next
        cur.next = Node(cur.val, next, None)
        cur = next

    cur = head
    new = dummy
    while cur:
        copy = cur.next
        copy.random = cur.random.next if cur.random else None
        cur = copy.next
        new.next, new = copy, copy

    return dummy.next

# [[7,null],[copy],[13,0],[copy],[11,4],[copy],[10,2],[copy],[1,0]]
