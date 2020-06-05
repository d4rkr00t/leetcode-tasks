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
        self.map = {}
        self.list = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False

        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False

        idx = self.map[val]
        del self.map[val]

        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]

        if self.list[idx] in self.map:
            self.map[self.list[idx]] = idx

        self.list.pop()


        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return self.list[random.randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
