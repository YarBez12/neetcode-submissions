class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsPerAmount = [0]
        for i in range(1, amount+1):
            curr = float("inf")
            for coin in coins:
                curr = min(curr, 1+coinsPerAmount[i-coin]) if i >= coin else curr
            coinsPerAmount.append(curr)
        return -1 if coinsPerAmount[-1] == float("inf") else coinsPerAmount[-1] 
        