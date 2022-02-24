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
    def reverse(f, t):
        prevHead = f
        cur = None

        while f != t:
            temp = f.next
            f.next = cur
            cur = f
            f = temp

        prevHead.next = t
        return cur

    cur = head
    dist = k
    while dist and cur:
        cur = cur.next
        dist -= 1

    if dist > 0:
        return head

    revHead = reverse(head, cur)
    head.next = reverseKGroup(cur, k)

    return revHead


ll = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                                                              ListNode(5))))))


def printList(ll):
    while ll:
        print(ll.val)
        ll = ll.next


printList(reverseKGroup(ll, 2))
