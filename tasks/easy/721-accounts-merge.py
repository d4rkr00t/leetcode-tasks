# Accounts Merge
# https://leetcode.com/problems/accounts-merge/
# medium
#
# Tags: Facebook, Amazon, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    pass


print(accountsMerge(
    [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]),
    [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
        ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
)
