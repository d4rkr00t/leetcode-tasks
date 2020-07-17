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
    ans = []

    def recur(expr, op, total, num):
        if not num:
            if total == target and len(expr) > 2:
                ans.append("".join([str(i) for i in expr]))
            return

        cur = expr.pop()
        n = int(num[0])
        num = num[1:]
        if cur != 0:
            next = op * 10 + n
            expr.append(next)
            recur(expr, next, total - cur + next, num)
            expr.pop()
        expr.append(cur)

        expr.append("+")
        expr.append(n)
        recur(expr, n, total + n, num)
        expr.pop()
        expr.pop()

        expr.append("-")
        expr.append(n)
        recur(expr, -n, total - n, num)
        expr.pop()
        expr.pop()

        expr.append("*")
        expr.append(n)
        recur(expr, n * op, total - op + (op*n), num)
        expr.pop()
        expr.pop()

    recur([int(num[0])], int(num[0]), int(num[0]), num[1:])

    return ans


print(addOperators(num="123", target=6), ["1+2+3", "1*2*3"])
print(addOperators(num="232", target=8), ["2*3+2", "2+3*2"])
print(addOperators(num="105", target=5), ["1*0+5", "10-5"])
print(addOperators(num="00", target=0), ["0+0", "0-0", "0*0"])
print(addOperators(num="3456237490", target=9191), [])
