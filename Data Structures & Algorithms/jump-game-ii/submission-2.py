class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        i = 0
        count = 0
        while i + nums[i] < len(nums)-1:
            count += 1
            best = i
            for j in range(i+1, min(len(nums), i+nums[i]+1)):
                if j + nums[j] > best + nums[best]:
                    best = j
            if best == i:
                return -1
            i = best
        return count + 1