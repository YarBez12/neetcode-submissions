class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for num in range(1,n+1):
            for j in range(1, int(num ** 0.5)+1):
                dp[num] = min(dp[num], dp[num-j**2]+1)
        return dp[-1]