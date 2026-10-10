class Solution:
    def isHappy(self, n: int) -> bool:
        got = set()
        while True:
            currSum = 0
            while n:
                currSum += (n % 10) ** 2
                n //= 10
            if currSum in got:
                return False
            if currSum == 1:
                return True
            got.add(currSum)
            n = currSum
        