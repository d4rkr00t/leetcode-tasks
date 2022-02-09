# Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD
import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.table:
            return False

        pos = len(self.list)
        self.table[val] = pos
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.table:
            return False

        pos = self.table[val]
        last = self.list[-1]
        self.table[last] = pos
        self.list[pos], self.list[-1] = self.list[-1], self.list[pos]
        self.list.pop()
        del self.table[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# { 1: 0, 3: 1 }
# [1, 3]
