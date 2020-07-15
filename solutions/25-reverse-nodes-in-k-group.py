# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# hard
#
# Tags: Microsoft, Amazon, Facebook
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dist = 0
    ptr = head

    def reverse(node, size):
        new_head, ptr = None, node

        while size:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            size -= 1

        return new_head

    while dist < k and ptr:
        ptr = ptr.next
        dist += 1

    if dist == k:
        reversed_head = reverse(head, k)
        head.next = reverseKGroup(ptr, k)
        return reversed_head

    return head


# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5
