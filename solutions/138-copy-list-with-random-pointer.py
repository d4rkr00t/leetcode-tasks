# Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    dummy = Node(None, None, None)
    cur = head
    table = {}

    while cur:
        table[cur] = table.get(cur, Node(cur.val, cur.next))
        cur = cur.next

    cur = dummy
    while head:
        cur.next = table[head]
        if head.random:
            cur.next.random = table[head.random]

        cur = cur.next

    return dummy.next
