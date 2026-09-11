class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # cost[i][j] = minimum changes needed
        # to make s[i:j+1] a palindrome
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        # dp[p][i] = minimum changes to partition
        # first i characters into p palindromes
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for p in range(1, k + 1):
            # Need at least p characters for p non-empty substrings
            for i in range(p, n + 1):

                # j = start of the last substring
                for j in range(p - 1, i):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]