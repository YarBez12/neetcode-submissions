class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i + nums[i] < len(nums)-1:
            best = i
            bestJump = i + nums[i]
            for j in range(i+1, min(len(nums), i+nums[i]+1)):
                curr = j + nums[j]
                if curr > bestJump:
                    best = j
                    bestJump = curr
            if best == i:
                return False
            i = best
        return True
