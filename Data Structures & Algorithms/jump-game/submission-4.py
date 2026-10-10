class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = 0
        for i in range(len(nums)):
            if canReach < i:
                return False
            canReach = max(canReach, i+nums[i])
        return True
