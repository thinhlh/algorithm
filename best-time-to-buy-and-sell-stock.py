class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # dp = [0] + [0] * len(prices)
        # for i in range(1, len(prices)+1):
        #     print(dp)
        #     if dp[i-1] + prices[i-1] < prices[i]:
        #         dp[i] = 0
        #     else:
        #         dp[i] = prices[i]-prices[i-1] + dp[i-1]

        #     # if prices[i-1] - dp[i-1] > -prices[i-1]:
        #     #     dp[i] = prices[i-1] - prices[i-2] + dp[i-1]
        #     # else:
        #     #     dp[i] = -prices[i-1]
        #     # dp[i] = max(prices[i-1] - prices[i-2] + dp[i-1], - prices[i-1])
        # print(dp)
        # return max(dp)
        # pass

        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
