class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        p1, p2, p3 = 0,1,1
        for i in range(2,n):
            p1, p2, p3 = p2, p3, p1+p2+p3
        return p3
        