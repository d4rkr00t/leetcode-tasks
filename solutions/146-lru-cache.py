# LRU Cache
# https://leetcode.com/problems/lru-cache/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(1)
# Space: O(n)
#
# Solution:
# Hash Table + Linked List


class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __remove__(self, key):
        self.size -= 1

        node = self.table[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.table[key]

    def __insert__(self, key, val):
        self.size += 1

        node = ListNode(key, val)
        self.table[key] = node

        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def __pop__(self):
        key = self.head.next.key
        self.__remove__(key)

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.__remove__(node.key)
            self.__insert__(node.key, node.val)
            return node.val

        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.table:
            self.__remove__(key)

        self.__insert__(key, val)

        if self.size > self.capacity:
            self.__pop__()


# c = 2
# size = 1
# table: {1: Node(1, 1), 2: Node(2, 2) }
# list: H <-> 2 <-> T
# put (1, 1)
# put (2, 2)
# get 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
