# LRU Cache
# https://leetcode.com/problems/lru-cache/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  O(1)
# Space: O(n)


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.table = {}

    def __insert__(self, node):
        self.size += 1

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.table[node.key] = node

    def __remove__(self, node):
        self.size -= 1

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        del self.table[node.key]

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.__remove__(node)
            self.__insert__(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            self.__remove__(self.table[key])

        node = Node(key, value)
        self.__insert__(node)

        if self.capacity < self.size:
            self.__remove__(self.tail.prev)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
