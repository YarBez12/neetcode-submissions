class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0
        }
        ans = 0
        n1 = len(num1)
        n2 = len(num2)
        for i1 in range(n1):
            curr = 0
            d1 = digits[num1[i1]]
            if d1 == 0:
                continue
            for i2 in range(n2):
                d2 = digits[num2[i2]]
                curr +=  d1 * d2 * (10 ** (n2-i2-1))


            ans += curr * (10 ** (n1-i1-1))
        return str(ans)
        