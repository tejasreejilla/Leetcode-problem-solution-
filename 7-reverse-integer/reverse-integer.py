class Solution:
    def reverse(self, x: int) -> int:
        y = x

        if x < 0:
            x = -x

        rev = 0
        while x:
            s = x % 10
            rev = rev * 10 + s
            x //= 10

        if y < 0:
            rev = -rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev