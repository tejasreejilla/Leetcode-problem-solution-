class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        unique = 9
        available = 9

        for digits in range(2, n + 1):
            unique *= available
            total += unique
            available -= 1

        return total