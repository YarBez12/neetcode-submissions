class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1st approach

        # n = len(nums)
        # req = n * (n+1) // 2
        # s = 0
        # for num in nums:
        #     s += num
        # return req - s


        # 2nd approach

        x = 0
        for i in range(len(nums)+1):
            x ^= i 
        for num in nums:
            x ^= num
        return x
        