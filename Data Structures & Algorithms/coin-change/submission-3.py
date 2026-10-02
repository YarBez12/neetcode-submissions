class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsPerAmount = [float("inf")] * (amount + 1)
        coinsPerAmount[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                coinsPerAmount[i] = min(coinsPerAmount[i], 1+coinsPerAmount[i-coin]) if i >= coin else coinsPerAmount[i]
        return -1 if coinsPerAmount[-1] == float("inf") else coinsPerAmount[-1] 
        