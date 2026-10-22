class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 1st approach 

            # if n % 2:
            #     count += 1
            # n = n // 2

            # 2nd approach
            n = (n) & (n-1)
            count += 1
        return count
        