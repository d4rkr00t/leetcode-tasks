# Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# medium
#
# Tags:
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for n in tokens:
        if n == "*":
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        elif n == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif n == "+":
            a, b = stack.pop(), stack.pop()
            stack.append(b + a)
        elif n == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        else:
            stack.append(int(n))

    return stack[-1]


print(evalRPN(["2", "1", "+", "3", "*"]), 9)
print(evalRPN(["4", "13", "5", "/", "+"]), 6)
print(
    evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
    22)
