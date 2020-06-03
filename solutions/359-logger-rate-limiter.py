# Logger Rate Limiter
# https://leetcode.com/problems/logger-rate-limiter/
# easy
#
# Tags: Google
#
# Time:  O(1)
# Space: O(n)
#
# Solution:
# HashTable

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}
        self.threashold = 10


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        if not message in self.messages or timestamp - self.messages[message] >= self.threashold:
            self.messages[message] = timestamp
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
