# Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/
# medium
#
# Tags: Facebook, Google, Microsoft
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    pushed.reverse()
    popped.reverse()
    stack = []

    while pushed and popped:
        stack.append(pushed.pop())
        while stack and popped and stack[-1] == popped[-1]:
            stack.pop()
            popped.pop()

    return not stack


# 1 2 3 4 5
# 4 5 3 2 1

print(validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]),
      True)
print(validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]),
      False)

# 1 2 3 4 5
#           |
# 4 3 5 1 2
#       |
# 1 2
