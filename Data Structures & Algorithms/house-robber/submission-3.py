class Solution:
    def rob(self, nums: List[int]) -> int:
        #1st approach 

        # if len(nums) <= 2:
        #     return max(nums)
        # ans = [nums[0], max(nums[0],nums[1])]
        # for i in range(2, len(nums)):
        #     ans.append(max(ans[i-2]+nums[i], ans[i-1]))
        # return ans[-1]

        #2nd approach 
        
        if len(nums) <= 2:
            return max(nums)
        p1 = max(nums[0],nums[1])
        p2 = nums[0]
        for i in range(2, len(nums)):
            t = max(p2 + nums[i], p1)
            p2 = p1
            p1 = t
        return p1
        