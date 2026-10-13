class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                dp[left][right] = float('inf')

                for guess in range(left, right):
                    cost = guess + max(
                        dp[left][guess - 1],
                        dp[guess + 1][right]
                    )
                    dp[left][right] = min(dp[left][right], cost)

        return dp[1][n]