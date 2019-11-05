class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        # i: day    j: order  k:has_order
        # 0<=i<=n-1,0<=j<=3,k in (0,1)
        import sys
        dp = [ [ [0,0],[0,0],[0,0] ] for i in range(n)]
        dp[0][2][0] = 0
        dp[0][1][0] = dp[0][2][1] = dp[0][0][0] = dp[0][0][1] = -sys.maxsize
        dp[0][1][1] = -prices[0]
        for i in range(1,n):
            for j in range(2):
                    # 买入时订单数-1,卖出时订单数不变
                    dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j+1][0] - prices[i])
        # 选择卖出股票中无论订单数最大的值
        ret = max(dp[n-1][0][0],dp[n-1][1][0])
        # 若赔钱，则不进行购买
        return ret if ret>0 else 0