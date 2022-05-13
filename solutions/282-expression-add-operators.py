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

    def calc(idx, prev_op, cur_op, val, expr):
        if idx == N:
            if target == val and cur_op == 0:
                ans.append("".join(expr[1:]))
            return

        cur_op = cur_op * 10 + int(num[idx])
        str_op = str(cur_op)

        if cur_op > 0:
            calc(idx + 1, prev_op, cur_op, val, expr)

        expr.append("+")
        expr.append(str_op)
        calc(idx + 1, cur_op, 0, val + cur_op, expr)
        expr.pop()
        expr.pop()

        if expr:
            expr.append("-")
            expr.append(str_op)
            calc(idx + 1, -cur_op, 0, val - cur_op, expr)
            expr.pop()
            expr.pop()

            expr.append("*")
            expr.append(str_op)
            calc(idx + 1, cur_op * prev_op, 0,
                 val - prev_op + (prev_op * cur_op), expr)
            expr.pop()
            expr.pop()

    calc(0, 0, 0, 0, [])
    return ans


print(addOperators(num="123", target=6), ["1+2+3", "1*2*3"])
print(addOperators(num="232", target=8), ["2*3+2", "2+3*2"])
print(addOperators(num="105", target=5), ["1*0+5", "10-5"])
print(addOperators(num="00", target=0), ["0+0", "0-0", "0*0"])
print(addOperators(num="3456237490", target=9191), [])
