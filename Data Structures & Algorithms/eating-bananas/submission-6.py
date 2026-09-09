class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1 
        if len(piles) == h:
            return max(piles)
        ans = max(piles)
        l = 1
        r = ans
        while l <= r:
            k = (l + r) // 2
            k = max(1, k)
            curr = 0
            for pile in piles:
                curr += math.ceil(pile / k)
            if curr > h:
                l = k + 1
            else:
                ans = min(ans, k)
                r = k - 1
        return ans