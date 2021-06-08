# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# medium
#
# Tags: Amazon, Facebook, Microsoft
#
# Time:  O(n)
# Space: O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    slow = fast = dummy

    while fast.next:
        if n <= 0:
            slow = slow.next

        fast = fast.next
        n -= 1

    slow.next = slow.next.next

    return dummy.next


# H -> 1 -> 2 -> 3 -> 4 -> 5
#                ^
#                          ^
# n = 0

# H -> 1, n = 1
# ^    ^
