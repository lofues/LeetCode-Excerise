class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0: return 0
        # 二维状态数组表示i , buy   第i天，是否持有股票，值为max_prices
        dp = [[0,0] for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[n-1][0]