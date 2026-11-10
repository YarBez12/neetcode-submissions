class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            c = defaultdict(int)
            # for i in range(s, -s-1, -1):
            #     c[i] += dp[i-num] + dp[i+num]
            for k, v in dp.items():
                c[k-num] += v
                c[k+num] += v
            dp = c
        return dp[target]
            
        # if not nums:
        #     if target == 0:
        #         return 1
        #     return 0
        # return self.findTargetSumWays(nums[:-1], target - nums[-1]) + self.findTargetSumWays(nums[:-1], target + nums[-1])
        