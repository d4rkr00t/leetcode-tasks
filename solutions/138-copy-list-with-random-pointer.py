# Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# medium
#
# Tags: Amazon, Microsoft, Facebook
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    cur = head

    while cur:
        node = Node(cur.val, cur.next, cur.random)
        cur.next = node
        cur = node.next

    cur = head
    while cur:
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    cur = head
    cur_new = head.next
    new_head = head.next

    while cur:
        cur.next = cur.next.next
        cur_new.next = cur_new.next.next if cur_new.next else None

        cur = cur.next
        cur_new = cur_new.next

    return new_head
