class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        x = self.find(n)
        y = n // x
        if y == 1:
            return n
        return self.minSteps(y) + x

    def find(self, n: int) -> int:
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return i
            i += 1
        return n
        