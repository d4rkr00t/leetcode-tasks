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
    stack = []
    pushed.reverse()
    popped.reverse()

    while pushed and popped:
        push = pushed.pop()
        stack.append(push)

        while popped and stack and stack[-1] == popped[-1]:
            stack.pop()
            popped.pop()

    return not stack


print(validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]),
      True)
print(validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]),
      False)
