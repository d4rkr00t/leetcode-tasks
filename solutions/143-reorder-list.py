# Reorder List
# https://leetcode.com/problems/reorder-list/
# medium
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# TBD

def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    arr = []
    node = head

    while node:
        arr.append(node)
        node = node.next

    node = head
    i = 1
    j = len(arr) - 1

    while i <= j:
        if i == j:
            node.next = arr[i]
            node.next.next = None
            break

        node.next = arr[j]
        node = node.next
        node.next = arr[i]
        node = node.next
        node.next = None
        i += 1
        j -= 1

    print(head)

# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 5 -> 2 -> 4 -> 3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
