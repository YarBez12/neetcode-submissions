class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        ans1 = [nums[0], max(nums[0],nums[1])]
        for i in range(2, len(nums)-1):
            ans1.append(max(ans1[i-2]+nums[i], ans1[i-1]))
        ans2 = [0, nums[1]]
        for i in range(2, len(nums)):
            ans2.append(max(ans2[i-2]+nums[i], ans2[i-1]))
        return max(ans1[-1], ans2[-1])
        