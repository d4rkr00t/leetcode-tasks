# Logger Rate Limiter
# https://leetcode.com/problems/logger-rate-limiter/
# easy
#
# Tags: Google
#
# Time:  O(1)
# Space: O(N)
#
# Solution:
# TBD


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp - self.table.get(message, 0) >= 10:
            self.table[message] = timestamp
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
