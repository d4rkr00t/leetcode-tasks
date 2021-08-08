# Three Divisors
# https://leetcode.com/problems/three-divisors/
# easy


def isThree(n: int) -> bool:
    divisors = 2

    for i in range(2, n):
        if n % i == 0:
            divisors += 1

        if divisors > 3:
            return False

    return divisors == 3


print(isThree(1), False)
print(isThree(2), False)
print(isThree(4), True)
print(isThree(5), False)
print(isThree(11), False)
