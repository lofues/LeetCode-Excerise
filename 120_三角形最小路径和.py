class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0: return 0
        dp = [[0] * i for i in range(1,n+1)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])