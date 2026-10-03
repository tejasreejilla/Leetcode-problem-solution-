class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        k = len(primes)

        ugly = [1] * n
        indices = [0] * k

        for i in range(1, n):
            # Find the smallest next candidate
            next_ugly = min(
                primes[j] * ugly[indices[j]]
                for j in range(k)
            )

            ugly[i] = next_ugly

            # Advance every pointer that produced this number
            for j in range(k):
                if primes[j] * ugly[indices[j]] == next_ugly:
                    indices[j] += 1

        return ugly[-1]