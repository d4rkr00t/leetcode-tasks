# Expression Add Operators
# https://leetcode.com/problems/expression-add-operators/
# hard
#
# Tags: Facebook, Google
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from typing import List


def addOperators(num: str, target: int) -> List[str]:
    ans = []
    N = len(num)

    def recur(index, prev_operand, current_operand, value, string):
        if index == N:
            if value == target and current_operand == 0:
                ans.append("".join(string[1:]))
            return

        current_operand = current_operand * 10 + int(num[index])
        str_op = str(current_operand)

        if current_operand > 0:
            recur(index + 1, prev_operand, current_operand,
                  value, string)

        string.append("+")
        string.append(str_op)
        recur(index + 1, current_operand, 0, value + current_operand, string)
        string.pop()
        string.pop()

        if string:
            string.append("-")
            string.append(str_op)
            recur(index + 1, -current_operand, 0,
                  value - current_operand, string)
            string.pop()
            string.pop()

            string.append("*")
            string.append(str_op)
            recur(index + 1, current_operand * prev_operand, 0,
                  value - prev_operand + (current_operand * prev_operand), string)
            string.pop()
            string.pop()

    recur(0, 0, 0, 0, [])

    return ans


print(addOperators(num="123", target=6), ["1+2+3", "1*2*3"])
print(addOperators(num="232", target=8), ["2*3+2", "2+3*2"])
print(addOperators(num="105", target=5), ["1*0+5", "10-5"])
print(addOperators(num="00", target=0), ["0+0", "0-0", "0*0"])
print(addOperators(num="3456237490", target=9191), [])
