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
    table = {}
    newHead = Node(0)
    cur = newHead
    node = head

    while node:
        nodeCopy = table.get(node, Node(node.val))
        cur.next = nodeCopy
        if node.random:
            randomNodeCopy = table.get(node, Node(node.random.val))
            table[node.random] = randomNodeCopy
            nodeCopy.random = randomNodeCopy

        node = node.next
        cur = cur.next

    return newHead.next
