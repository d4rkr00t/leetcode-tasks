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
        self.ht = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.ht:
            return False

        self.ht[val] = val
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.ht:
            del self.ht[val]
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        keys = self.ht.keys()
        r = random.randint(0, len(keys)-1)

        return self.ht[keys[r]]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
