class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l, r = 0, x // 2
        while l <= r:
            m = (l + r) // 2
            res = m * m 
            if res == x:
                return m
            if res > x:
                r = m - 1
            else:
                l = m + 1
        
        return l-1