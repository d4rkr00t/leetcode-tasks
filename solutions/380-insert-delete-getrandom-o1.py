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

from random import choice


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.table:
            return False

        self.table[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.table:
            return False

        idx = self.table[val]
        val2 = self.arr[-1]
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        self.arr.pop()
        self.table[val2] = idx
        del self.table[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
