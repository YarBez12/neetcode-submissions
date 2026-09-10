class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        l = 0
        r = len(nums)-1
        part = 0 if target >= nums[0] else 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > nums[0] and part == 1:
                l = m + 1
            elif nums[m] > nums[0] and part == 0:
                if nums[m] > target:
                    r = m -1
                else:
                    l = m + 1
            elif nums[m] < nums[0] and part == 0:
                r = m - 1
            elif nums[m] < nums[0] and part == 1:
                if nums[m] > target:
                    r = m -1
                else:
                    l = m + 1
            else:
                l = m + 1
        
        return -1
        