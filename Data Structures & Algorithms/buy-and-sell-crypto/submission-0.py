class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        ans = 0
        for i in range(len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            else:
                ans = max(ans, prices[i] - curr)
        return ans
        