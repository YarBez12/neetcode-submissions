class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        ans = [nums[0], max(nums[0],nums[1])]
        for i in range(2, len(nums)):
            ans.append(max(ans[i-2]+nums[i], ans[i-1]))
        return ans[-1]
        