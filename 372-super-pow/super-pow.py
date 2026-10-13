from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        result = 1

        for digit in b:
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD

        return result

