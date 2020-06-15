# Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/
# hard
#
# Tags: Facebook, Amazon, Google
#
# Time:  O(2^n)
# Space: O(2^n)
#
# Solution:
# Backtracking

def removeInvalidParentheses(s: str) -> [str]:
    valid = set()
    min_removed = float("inf")

    def backtrack(s, cur, pos, left_count, right_count, removed):
        nonlocal min_removed, valid

        if pos == len(s):
            if left_count == right_count:
                if removed < min_removed:
                    valid = set()
                    min_removed = removed

                if removed <= min_removed:
                    valid.add(cur)

            return

        next_left_count = left_count + 1 if s[pos] == "(" else left_count
        next_right_count = right_count + 1 if s[pos] == ")" else right_count


        if next_left_count - next_right_count >= 0:
            backtrack(s, cur + s[pos], pos + 1, next_left_count, next_right_count, removed)

        backtrack(s, cur, pos + 1, left_count, right_count, removed + 1)

    backtrack(s, "", 0, 0, 0, 0)
    return list(valid)

print(removeInvalidParentheses("()())()"), ["()()()", "(())()"])
print(removeInvalidParentheses("(a)())()"), ["(a)()()", "(a())()"])
print(removeInvalidParentheses(")("), [])
