# Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# medium
#
# Tags: Google, Amazon
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import math
from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []

    def apply(operator, op1, op2):
        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        elif operator == "/":
            return int(op1 / op2)

    for t in tokens:
        if t in ("+", "-", "*", "/"):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(apply(t, op2, op1))
        else:
            stack.append(int(t))

    return stack[-1]


print(evalRPN(["2", "1", "+", "3", "*"]), 9)
print(evalRPN(["4", "13", "5", "/", "+"]), 6)
print(
    evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
    22)
