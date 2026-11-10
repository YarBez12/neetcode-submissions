class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        fullSum = sum(nums)
        if fullSum % 2:
            return False
        req = fullSum // 2
        dp = [False] * (req+1)
        dp[0] = True
        
        for num in nums:
            # c = dp[:]
            # for i in range(req+1):
            #     if i + num < req+1 and dp[i]:
            #         c[i+num] = True
            # dp = c
            for i in range(req,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        return dp[-1]
