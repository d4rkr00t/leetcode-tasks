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

def addOperators(num: str, target: int) -> [str]:
    # 4 cases
    # 1. pick next char
    # 2. add
    # 3. substract
    # 4. multiply

    ans = []

    def backtrack(expr, p_op, c_op, pos, total):
        if pos == len(num):
            if target == total and c_op == 0:
                ans.append("".join(expr[1:]))

            return

        c_op = c_op * 10 + int(num[pos])
        str_op = str(c_op)

        if c_op > 0:
            backtrack(expr, p_op, c_op, pos + 1, total)

        # 2. add
        expr.append("+")
        expr.append(str_op)
        backtrack(expr, c_op, 0, pos + 1, total + c_op)
        expr.pop()
        expr.pop()

        if not expr: return

        # 3. substract
        expr.append("-")
        expr.append(str_op)
        backtrack(expr, -c_op, 0, pos + 1, total - c_op)
        expr.pop()
        expr.pop()

        # 4. mul
        expr.append("*")
        expr.append(str_op)
        backtrack(expr, c_op * p_op, 0, pos + 1, total - p_op + (c_op * p_op))
        expr.pop()
        expr.pop()

    backtrack([], 0, 0, 0, 0)

    return ans

print(addOperators(num = "123", target = 6), ["1+2+3", "1*2*3"])
print(addOperators(num = "232", target = 8), ["2*3+2", "2+3*2"])
print(addOperators(num = "105", target = 5), ["1*0+5","10-5"])
print(addOperators(num = "00", target = 0), ["0+0", "0-0", "0*0"])
print(addOperators(num = "3456237490", target = 9191), [])
