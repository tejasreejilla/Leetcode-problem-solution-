class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initial states
        hold = -prices[0]  # Bought stock on day 0
        sold = 0           # Sold stock today
        cooldown = 0       # Not holding stock

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_cooldown = cooldown

            # Either keep holding, or buy today after cooldown
            hold = max(prev_hold, prev_cooldown - price)

            # Sell the stock today
            sold = prev_hold + price

            # Either continue cooldown/resting, or enter cooldown
            # after selling yesterday
            cooldown = max(prev_cooldown, prev_sold)

        return max(sold, cooldown)
