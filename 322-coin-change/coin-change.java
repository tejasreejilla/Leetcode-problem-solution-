class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];

        // Impossible value
        int INF = amount + 1;

        // Initialize
        for (int i = 1; i <= amount; i++) {
            dp[i] = INF;
        }

        dp[0] = 0;

        // Build the answer for every amount
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {

                if (coin <= i) {
                    dp[i] = Math.min(
                        dp[i],
                        dp[i - coin] + 1
                    );
                }
            }
        }

        return dp[amount] == INF ? -1 : dp[amount];
    }
}