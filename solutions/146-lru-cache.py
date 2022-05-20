# LRU Cache
# https://leetcode.com/problems/lru-cache/
# medium
#
# Tags: Amazon, Microsoft, Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


class Node:
    def __init__(self, key=0, value=0, prev=None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

        self.nodes = {}
        self.capacity = capacity
        self.size = 0

    def __pop__(self):
        if self.size == 0:
            return

        node = self.head.next
        self.__remove__(node)

    def __remove__(self, node):
        del self.nodes[node.key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size -= 1

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.__remove__(node)
            self.put(node.key, node.val)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if self.size + 1 > self.capacity:
            self.__pop__()

        prev = self.tail.prev
        node = Node(key, value)

        node.next = self.tail
        prev.next = node
        self.tail.prev = node

        self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
