class Solution:

    # 1st approach

    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return x
    #     if n < 0:
    #         return 1 / self.myPow(x, -n)
    #     i = n // 2
    #     half = self.myPow(x, i)
    #     res = half * half
    #     return res if n % 2 == 0 else res * x
        

    # 2nd approach

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        currentProduct = x
        while n > 0:
            if n % 2 == 1:
                res *= currentProduct
            currentProduct *= currentProduct
            n //= 2
        return res