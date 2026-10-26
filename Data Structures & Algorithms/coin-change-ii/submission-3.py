class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0] * (amount+1) for i in range(len(coins)+1)]
        dp[0][0] = 1
        for i in range(len(coins)):
            for j in range(amount+1):
                if coins[i] <= j:
                    dp[i+1][j] += dp[i+1][j-coins[i]]
                dp[i+1][j] += dp[i][j]
        return dp[-1][amount]
        