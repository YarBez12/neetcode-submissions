class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1 
        if len(piles) == h:
            return max(piles)
        l = 1
        r = max(piles)
        while l <= r:
            k = (l + r) // 2
            curr = 0
            for pile in piles:
                curr += math.ceil(pile / k)
            if curr > h:
                l = k + 1
            else:
                r = k - 1
        return l