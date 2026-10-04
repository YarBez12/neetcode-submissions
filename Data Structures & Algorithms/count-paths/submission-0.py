class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                delta = 0
                if i != 0:
                    delta += dp[i-1][j]
                if j != 0:
                    delta += dp[i][j-1]
                dp[i][j] += delta
        return dp[-1][-1]
        