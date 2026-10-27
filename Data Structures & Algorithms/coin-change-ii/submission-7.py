class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        # for i in range(len(coins)):
        for coin in coins:
            # for j in range(amount+1):
            for j in range(coin, amount+1):
                # if coins[i] <= j:
                # dp[j] += dp[j-coins[i]]
                dp[j] += dp[j-coin]
                ## dp[i+1][j] += dp[i][j]
        return dp[amount]
        