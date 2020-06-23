# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# hard
#
# Tags: Microsoft, Amazon, Facebook
#
# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLinkedList(head, k):
    new_head,ptr = None, head

    while k:
        next_node = ptr.next
        ptr.next = new_head
        new_head = ptr
        ptr = next_node
        k -= 1

    return new_head

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    ptr = head
    ktail = None
    new_head = None

    while ptr:
        count = 0
        ptr = head

        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count != k: continue

        rev_head = self.reverseLinkedList(head, k)

        if not new_head:
            new_head = rev_head

        if ktail:
            ktail.next = rev_head

        ktail = head
        head = ptr


    if ktail:
        ktail.next = head

    return new_head if new_head else head

# def reverseKGroup(head: ListNode, k: int) -> ListNode:
#     count = 0
#     ptr = head

#     while count < k and ptr:
#         ptr = ptr.next
#         count += 1

#     if count != k:
#         return head

#     reversed_head = reverseLinkedList(head, k)
#     head.next = self.reverseKGroup(ptr, k)
#     return reversed_head

# 1 -> 2 -> 3 -> 4
