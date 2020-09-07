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
    new_head = cur = Node()
    table = {}

    while head:
        clone = table.get(head, Node(head.val))
        table[head] = clone
        cur.next = clone

        if head.random:
            random_link = table.get(head.random, Node(head.random.val))
            table[head.random] = random_link
            clone.random = random_link

        cur = cur.next
        head = head.next

    return new_head.next
