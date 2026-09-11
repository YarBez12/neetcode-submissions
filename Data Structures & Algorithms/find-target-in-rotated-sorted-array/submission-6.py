class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #1st approach 

        # if len(nums) == 1:
        #     return 0 if target == nums[0] else -1
        # l = 0
        # r = len(nums)-1
        # part = 0 if target >= nums[0] else 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] > nums[0] and part == 0 and nums[m] >= target:
        #         r = m -1
        #     elif nums[m] > nums[0]:
        #         l = m + 1
        #     elif nums[m] < nums[0] and part == 1 and nums[m] < target:
        #         l = m + 1
        #     elif nums[m] < nums[0]:
        #         r = m - 1
        
        # return -1


        #2nd approach 

        l = 0
        r = len(nums)-1
        part = 0 if target >= nums[0] else 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
        