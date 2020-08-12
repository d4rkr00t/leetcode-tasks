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

class LLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.head = LLNode(None, None)
        self.tail = LLNode(None, None)
        self.table = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.table.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.table.get(key)

        if not node:
            newNode = LLNode(key, value)
            self.table[key] = newNode
            self._add_node(newNode)
            self.len += 1

            if self.len > self.capacity:
                tail = self._pop_tail()
                del self.table[tail.key]
                self.len -= 1
        else:
            node.val = value
            self._move_to_head(node)
