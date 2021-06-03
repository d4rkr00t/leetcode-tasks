# Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# medium
#
# Tags: Amazon, Facebook, Google, Microsoft
#
# Time:  O(1)
# Space: O(n)
#
# Solution:
# HashTable + Array

from random import randrange


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

        self.table[val] = len(self.list)
        self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.table:
            return False

        idx = self.table[val]
        val2 = self.list[-1]
        self.list[-1], self.list[idx] = self.list[idx], self.list[-1]
        self.list.pop()
        self.table[val2] = idx
        del self.table[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.list[randrange(len(self.list))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
